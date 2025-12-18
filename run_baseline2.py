#第二版，基于已经事先生成好的变异体，生成unit test进行测试，双卡并行生成
import json
import os
import shutil
import subprocess
import re
import sys
import ast
import time
from tqdm import tqdm
from vllm import LLM, SamplingParams

# ================= 0. 配置 =================
# 原始题目数据 (用于生成 Prompt)
DATA_PATH = "./datasets/CodeRM-filter/mist_test_cf.jsonl"
# 预生成的变异体目录 (Phase 0 的产物)
MUTANT_SOURCE_DIR = "./mut_generate/mist_test_cf" 
# 模型路径
MODEL_PATH = "./model/CodeRM-8B"
# 结果输出目录
BASE_OUTPUT_DIR = "./mut_cp"
REPORT_DIR = "./results"
REPORT_FILE = os.path.join(REPORT_DIR, "final_report.json")

BATCH_SIZE = 10 

# ================= 1. 工具函数 =================

def clean_output(text):
    """
    清洗代码：掐头 (Markdown/Import) + 去尾 (AST Truncate)
    """
    text = re.sub(r'```python', '', text)
    text = re.sub(r'```', '', text)
    
    # 掐头
    start_marker = "import unittest"
    idx = text.find(start_marker)
    if idx != -1:
        text = text[idx:]
    else:
        class_match = re.search(r'^class\s+\w+', text, re.MULTILINE)
        if class_match:
            text = "import unittest\n" + text[class_match.start():]
    
    text = text.strip()
    
    # 去尾 (AST)
    try:
        tree = ast.parse(text)
        if not tree.body: return text
        
        valid_nodes = []
        for node in tree.body:
            # 移除模型自己写的 main 函数
            if isinstance(node, ast.If) and isinstance(node.test, ast.Compare):
                try:
                    left = node.test.left
                    if isinstance(left, ast.Name) and left.id == "__name__":
                        continue
                except: pass
            valid_nodes.append(node)
            
        if valid_nodes:
            last_node = valid_nodes[-1]
            if hasattr(last_node, 'end_lineno'):
                end_line = last_node.end_lineno
                lines = text.split('\n')
                text = '\n'.join(lines[:end_line])
    except SyntaxError:
        pass 
    return text

def setup_task_env(task_id, solution_code, question_text, test_code, entry_point):
    """初始化环境，写入源码和测试代码"""
    task_dir = os.path.join(BASE_OUTPUT_DIR, task_id)
    os.makedirs(task_dir, exist_ok=True)
    
    # 写入 solution.py
    with open(os.path.join(task_dir, "solution.py"), "w", encoding='utf-8') as f:
        f.write(f'"""\nORIGINAL QUESTION:\n{question_text}\n"""\n\n{solution_code}')
    
    # 写入 test_suite.py
    lines = test_code.split('\n')
    cleaned_lines = [l for l in lines if not re.match(r'^from\s+solution\s+import', l.strip())]
    final_test_code = f"from solution import {entry_point}\n" + "\n".join(cleaned_lines)
    final_test_code += "\n\nif __name__ == '__main__':\n    unittest.main()\n"
    
    with open(os.path.join(task_dir, "test_suite.py"), "w", encoding='utf-8') as f:
        f.write(final_test_code)
    
    return task_dir

def load_mutants_from_disk(task_id):
    """
    从磁盘加载预生成的变异体
    路径: ./mut_generate/mist_test_cf/{task_id}/mutants.json
    """
    path = os.path.join(MUTANT_SOURCE_DIR, task_id, "mutants.json")
    if not os.path.exists(path):
        return []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("mutants", [])
    except Exception as e:
        print(f"Error loading mutants for {task_id}: {e}")
        return []

def execute_test(task_dir, timeout):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = task_dir + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(
            ["python3", "test_suite.py"], cwd=task_dir, capture_output=True, text=True, env=env, timeout=timeout
        )
        combined_output = result.stderr + "\n" + result.stdout
        return result.returncode, combined_output
    except subprocess.TimeoutExpired:
        return -999, "TIMEOUT"
    except Exception as e:
        return 1, str(e)

def parse_unittest_summary(output):
    if not output: return 0, 0, 0
    run_match = re.search(r"Ran (\d+) tests", output)
    run_count = int(run_match.group(1)) if run_match else 0
    fail_count = 0
    error_count = 0
    failures_match = re.search(r"failures=(\d+)", output)
    if failures_match: fail_count = int(failures_match.group(1))
    errors_match = re.search(r"errors=(\d+)", output)
    if errors_match: error_count = int(errors_match.group(1))
    if (fail_count == 0 and error_count == 0) and "FAILED" in output: fail_count = 1 
    return run_count, fail_count, error_count

def extract_failed_tests(output):
    failed = []
    if not output: return failed
    for line in output.split('\n'):
        if line.startswith("FAIL:") or line.startswith("ERROR:"):
            parts = line.split(' ')
            if len(parts) > 1: failed.append(parts[1])
    return failed

# ================= 2. 主流程 =================

def main():
    # 清理输出目录 (保留 REPORT_DIR)
    if os.path.exists(BASE_OUTPUT_DIR): shutil.rmtree(BASE_OUTPUT_DIR)
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)

    # 检查变异体源目录是否存在
    if not os.path.exists(MUTANT_SOURCE_DIR):
        print(f"❌ Error: Mutant source directory not found: {MUTANT_SOURCE_DIR}")
        print("Please run `generate_mut.py` first.")
        return

    # 加载题目数据
    with open(DATA_PATH, 'r') as f:
        all_data = [json.loads(line) for line in f if line.strip()]
    
    print(f"🚀 Loading CodeRM-8B...")
    llm = LLM(model=MODEL_PATH, tensor_parallel_size=2, dtype="bfloat16",max_model_len=8192)
    
    sampling_params = SamplingParams(
        temperature=0.2, 
        max_tokens=4096, 
        repetition_penalty=1.05,
        stop=["<|end_of_text|>"]
    )

    final_report = []

    print(f"\n🚀 Starting Evaluation (Using pre-generated mutants)...")

    for i in range(0, len(all_data), BATCH_SIZE):
        batch = all_data[i : i + BATCH_SIZE]
        print(f"\n[Batch {i//BATCH_SIZE + 1}] Processing items {i} to {i+len(batch)}...")
        
        # 1. Generate Prompts
        prompts = []
        for item in batch:
            p = (f"Below is a question and it's corresponding code answer. "
                 f"Please write test cases to check the correctness of the code answer. "
                 f"You need to use the unittest library in Python and create a test class for testing.\n\n"
                 f"### question\n{item.get('original_question', '')}\n\n"
                 f"### code solution\n{item['canonical_solution']}\n\n"
                 f"Please add detailed comments.")
            prompts.append(p)
        outputs = llm.generate(prompts, sampling_params)
        
        # 2. Process
        for j, output in enumerate(outputs):
            item = batch[j]
            task_id = item['task_id']
            solution_code = item['canonical_solution']
            
            # Setup Files
            test_code = clean_output(output.outputs[0].text)
            task_dir = setup_task_env(
                task_id, solution_code, item.get('original_question', ''), test_code, item['entry_point']
            )
            
            # === Step 1: 加载预生成的变异体 ===
            mutants = load_mutants_from_disk(task_id)
            print(f"  Task {task_id}: Load {len(mutants)} muts. ", end="", flush=True)
            
            # === Step 2: 跑源码 (Source Check) ===
            # 超时设为 60s
            ret_code, output_log = execute_test(task_dir, timeout=60)
            pass_source = (ret_code == 0)
            
            run_n, fail_n, err_n = parse_unittest_summary(output_log)
            failed_total = fail_n + err_n
            
            error_type = ""
            if ret_code == -999: error_type = "TIMEOUT"
            elif not pass_source: error_type = "ASSERT_FAIL" if run_n > 0 else "CRASH"

            source_check_info = {
                "passed": pass_source,
                "return_code": ret_code,
                "error_type": error_type,
                "stats": {"run": run_n, "failed": failed_total},
                "failed_cases": extract_failed_tests(output_log),
                "log_snippet": output_log[-500:] if output_log else ""
            }
            
            mutants_log = []
            mutation_stats = {"killed": 0, "total": len(mutants), "score": None}

            if not pass_source:
                # 终端输出失败原因
                if error_type == "TIMEOUT": print(f"❌ Source Fail (TIMEOUT > 60s).")
                elif run_n > 0: print(f"❌ Source Fail ({failed_total}/{run_n} failed).")
                else: print(f"❌ Source Fail (Crash/Syntax Error).")
                
                # 记录所有变异体为 SKIPPED，同时保留原始变异信息
                for m in mutants:
                    mutants_log.append({
                        "id": f"m_{m.get('lineno')}",
                        "operator": m.get('operator'),
                        "lineno": m.get('lineno'),
                        "original_line": m.get('original_line'), # <--- 你的需求
                        "mutated_line": m.get('mutated_line'),   # <--- 你的需求
                        "code": m.get('code'),                   # <--- 你的需求
                        "status": "SKIPPED_SOURCE_FAIL"
                    })
            else:
                print("✅ Source Pass.", end=" ", flush=True)
                if len(mutants) == 0:
                    print("⚠️ No mutants.")
                    mutation_stats["score"] = None
                else:
                    # === Step 3: 跑变异 (Mutation Execution) ===
                    print("Testing mutants...", end="", flush=True)
                    killed_count = 0
                    solution_path = os.path.join(task_dir, "solution.py")
                    shutil.copy(solution_path, solution_path + ".bak")
                    
                    try:
                        for idx, m in enumerate(mutants):
                            # 写入变异代码
                            with open(solution_path, "w", encoding='utf-8') as f:
                                f.write(m['code'])
                            
                            # 执行测试 (超时 15s)
                            m_ret, _ = execute_test(task_dir, timeout=15)
                            
                            is_killed = (m_ret != 0)
                            if is_killed: killed_count += 1
                            
                            status = "KILLED" if is_killed else "SURVIVED"
                            if m_ret == -999: status = "TIMEOUT_KILLED"
                            
                            # 记录详细日志（包含源码和变异代码）
                            mutants_log.append({
                                "id": f"m_{idx}",
                                "operator": m.get('operator'),
                                "lineno": m.get('lineno'),
                                "original_line": m.get('original_line'), # <--- 透传字段
                                "mutated_line": m.get('mutated_line'),   # <--- 透传字段
                                "code": m['code'],                       # <--- 透传完整代码
                                "status": status,
                                "killed": is_killed
                            })
                    finally:
                        shutil.move(solution_path + ".bak", solution_path)
                    
                    mutation_stats["killed"] = killed_count
                    mutation_stats["score"] = (killed_count / len(mutants)) * 100
                    print(f"🎯 Score: {mutation_stats['score']:.1f}%")

            # 保存结果到 task 目录
            with open(os.path.join(task_dir, "mutants.json"), "w", encoding='utf-8') as f:
                json.dump({
                    "task_id": task_id, 
                    "source_check": source_check_info,
                    "mutation_stats": mutation_stats, 
                    "mutants": mutants_log
                }, f, indent=2)

            final_report.append({
                "task_id": task_id, 
                "source_check": source_check_info, 
                "mutation_check": mutation_stats
            })

        # 实时保存总报告
        with open(REPORT_FILE, 'w') as f: json.dump(final_report, f, indent=2)

    # 最终统计
    valid_scores = [
        r['mutation_check']['score'] 
        for r in final_report 
        if r['source_check']['passed'] and r['mutation_check']['score'] is not None
    ]
    avg_score = sum(valid_scores)/len(valid_scores) if valid_scores else 0
    passed_cnt = sum(1 for r in final_report if r['source_check']['passed'])
    
    print("\n" + "="*40)
    print(f"REPORT SUMMARY")
    print(f"Pass@1: {passed_cnt}/{len(final_report)}")
    print(f"Valid Mutation Samples: {len(valid_scores)}")
    print(f"Avg Mutation Score: {avg_score:.2f}%")
    print("="*40)

if __name__ == "__main__":
    main()