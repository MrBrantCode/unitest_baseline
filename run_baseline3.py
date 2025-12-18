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
DATA_PATH = "./datasets/CodeRM-filter/mist_test_cf.jsonl"
MUTANT_SOURCE_DIR = "./mut_generate/mist_test_cf"
MODEL_PATH = "./model/CodeRM-8B"
BASE_OUTPUT_DIR = "./mut_cp"
REPORT_DIR = "./results"
REPORT_FILE = os.path.join(REPORT_DIR, "final_report.json")

BATCH_SIZE = 10 
N_SAMPLES = 3  # 每个题目生成 3 个候选测试

# ================= 1. 核心工具函数 (已升级) =================

def clean_output(text):
    """
    清洗代码 V4.0 (严师模式 + 防截断)
    1. 去除 Markdown
    2. 补充 import unittest (IDE式辅助)
    3. 防截断修剪 (因长度限制导致的 SyntaxError 可以修，但逻辑错误不修)
    4. 不自动修复 class 结构
    """
    # 1. 基础清洗
    text = re.sub(r'```python', '', text)
    text = re.sub(r'```', '', text)
    text = text.strip()

    # 2. 检查并补充 import unittest
    if "import unittest" not in text:
        text = "import unittest\n" + text

    # 3. 循环回退剪枝 (Anti-Truncation)
    lines = text.split('\n')
    valid_code = ""
    
    # 最多尝试回退 len(lines) 次
    for _ in range(len(lines)):
        if not lines: break
        
        current_attempt = '\n'.join(lines)
        try:
            # 尝试解析 AST
            tree = ast.parse(current_attempt)
            
            # === AST 过滤逻辑 ===
            valid_nodes = []
            for node in tree.body:
                # 过滤掉 if __name__ == "__main__": 
                # (防止模型写了 execution 逻辑，后面 setup_task_env 会统一加)
                if isinstance(node, ast.If) and isinstance(node.test, ast.Compare):
                    try:
                        left = node.test.left
                        if isinstance(left, ast.Name) and left.id == "__name__":
                            continue
                    except: pass
                valid_nodes.append(node)
                
            # 根据最后一个有效节点截断
            if valid_nodes:
                last_node = valid_nodes[-1]
                if hasattr(last_node, 'end_lineno'):
                    end_line = last_node.end_lineno
                    valid_code = '\n'.join(current_attempt.split('\n')[:end_line])
                else:
                    valid_code = current_attempt
            else:
                valid_code = current_attempt
            
            # 语法正确，跳出循环
            return valid_code

        except (SyntaxError, IndentationError):
            # 语法错误，说明可能断在半截，删掉最后一行重试
            lines.pop()
            
    # 如果剪完了还是不行，返回当前状态
    return valid_code if valid_code else text

def setup_task_env(task_id, solution_code, question_text, test_code, entry_point):
    """初始化环境，处理导入和入口"""
    task_dir = os.path.join(BASE_OUTPUT_DIR, task_id)
    os.makedirs(task_dir, exist_ok=True)
    
    # 写入 solution.py
    with open(os.path.join(task_dir, "solution.py"), "w", encoding='utf-8') as f:
        f.write(f'"""\nORIGINAL QUESTION:\n{question_text}\n"""\n\n{solution_code}')
    
    # 处理 test_suite.py
    lines = test_code.split('\n')
    # 过滤掉模型可能自己生成的 from solution import ...
    cleaned_lines = [l for l in lines if not re.match(r'^from\s+solution\s+import', l.strip())]
    
    # 注入正确的 Import 和 main 执行入口
    final_test_code = f"from solution import {entry_point}\n" + "\n".join(cleaned_lines)
    final_test_code += "\n\nif __name__ == '__main__':\n    unittest.main()\n"
    
    with open(os.path.join(task_dir, "test_suite.py"), "w", encoding='utf-8') as f:
        f.write(final_test_code)
    
    return task_dir

def load_mutants_from_disk(task_id):
    path = os.path.join(MUTANT_SOURCE_DIR, task_id, "mutants.json")
    if not os.path.exists(path): return []
    try:
        with open(path, 'r', encoding='utf-8') as f: return json.load(f).get("mutants", [])
    except: return []

def execute_test(task_dir, timeout):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = task_dir + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(["python3", "test_suite.py"], cwd=task_dir, capture_output=True, text=True, env=env, timeout=timeout)
        combined_output = result.stderr + "\n" + result.stdout
        return result.returncode, combined_output
    except subprocess.TimeoutExpired: return -999, "TIMEOUT"
    except Exception as e: return 1, str(e)

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
    if os.path.exists(BASE_OUTPUT_DIR): shutil.rmtree(BASE_OUTPUT_DIR)
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    # 检查变异体文件是否存在
    if not os.path.exists(MUTANT_SOURCE_DIR):
        print(f"❌ Error: Mutant source directory not found: {MUTANT_SOURCE_DIR}")
        return

    with open(DATA_PATH, 'r') as f:
        all_data = [json.loads(line) for line in f if line.strip()]
    
    print(f"🚀 Loading CodeRM-8B...")
    llm = LLM(model=MODEL_PATH, tensor_parallel_size=2, dtype="bfloat16", max_model_len=8192)
    
    # === Pass@3 采样配置 ===
    # 稍微提高 temperature (0.4) 增加多样性，max_tokens 设大防止截断（虽然有兜底）
    sampling_params = SamplingParams(
        n=N_SAMPLES,
        temperature=0.4, 
        max_tokens=4096, 
        repetition_penalty=1.05,
        stop=["<|end_of_text|>"]
    )

    final_report = []

    print(f"\n🚀 Starting Evaluation (Pass@{N_SAMPLES} Mode with Anti-Truncation)...")

    for i in range(0, len(all_data), BATCH_SIZE):
        batch = all_data[i : i + BATCH_SIZE]
        print(f"\n[Batch {i//BATCH_SIZE + 1}] Processing items {i} to {i+len(batch)}...")
        
        prompts = []
        for item in batch:
            p = (f"Below is a question and it's corresponding code answer. "
                 f"Please write test cases to check the correctness of the code answer. "
                 f"You need to use the unittest library in Python and create a test class for testing.\n\n"
                 f"### question\n{item.get('original_question', '')}\n\n"
                 f"### code solution\n{item['canonical_solution']}\n\n"
                 f"Please add detailed comments.")
            prompts.append(p)
        
        # 生成 N_SAMPLES 个候选
        outputs = llm.generate(prompts, sampling_params)
        
        for j, output in enumerate(outputs):
            item = batch[j]
            task_id = item['task_id']
            solution_code = item['canonical_solution']
            mutants = load_mutants_from_disk(task_id)
            
            print(f"  Task {task_id}: Load {len(mutants)} muts. ", end="", flush=True)
            
            # === Pass@K 循环逻辑 ===
            pass_source = False
            final_task_dir = None
            final_output_log = ""
            final_ret_code = 1
            status_icons = ""
            
            # 遍历 3 个候选代码
            for candidate_idx, candidate_output in enumerate(output.outputs):
                # 使用升级版 clean_output (带回退剪枝 + Import 补全)
                test_code = clean_output(candidate_output.text)
                
                # 写入硬盘 (每次覆盖之前的尝试，直到成功)
                task_dir = setup_task_env(
                    task_id, solution_code, item.get('original_question', ''), test_code, item['entry_point']
                )
                
                # 跑源码测试 (60s)
                ret_code, output_log = execute_test(task_dir, timeout=60)
                
                if ret_code == 0:
                    status_icons += "✅"
                    pass_source = True
                    final_task_dir = task_dir
                    final_output_log = output_log
                    final_ret_code = ret_code
                    # 成功了！跳出循环，不再试后面的候选
                    break 
                else:
                    status_icons += "❌"
                    # 失败了，暂存这次的结果，如果后面也没成功，就用最后一次的结果
                    final_output_log = output_log
                    final_ret_code = ret_code
                    final_task_dir = task_dir

            # 打印图标结果
            print(f"{status_icons} ", end="", flush=True)

            # === 后续逻辑 ===
            run_n, fail_n, err_n = parse_unittest_summary(final_output_log)
            failed_total = fail_n + err_n
            error_type = ""
            if final_ret_code == -999: error_type = "TIMEOUT"
            elif not pass_source: 
                if run_n > 0: error_type = "ASSERT_FAIL"
                else: error_type = "CRASH" # 包含 SyntaxError 或 NameError (比如没写 Class)

            source_check_info = {
                "passed": pass_source,
                "attempts_taken": len(status_icons),
                "trace": status_icons,
                "return_code": final_ret_code,
                "error_type": error_type,
                "stats": {"run": run_n, "failed": failed_total},
                "log_snippet": final_output_log[-500:] if final_output_log else ""
            }
            
            mutants_log = []
            mutation_stats = {"killed": 0, "total": len(mutants), "score": None}

            if not pass_source:
                # 源码没过
                print(f"Source Fail ({error_type}).")
                for m in mutants:
                    mutants_log.append({
                        "id": f"m_{m.get('lineno')}", "operator": m.get('operator'),
                        "status": "SKIPPED_SOURCE_FAIL"
                    })
            else:
                # 源码过了 -> 跑变异
                if len(mutants) == 0:
                    print("⚠️ No mutants.")
                    mutation_stats["score"] = None
                else:
                    print("Testing mutants...", end="", flush=True)
                    killed_count = 0
                    solution_path = os.path.join(final_task_dir, "solution.py")
                    shutil.copy(solution_path, solution_path + ".bak")
                    try:
                        for idx, m in enumerate(mutants):
                            with open(solution_path, "w", encoding='utf-8') as f: f.write(m['code'])
                            m_ret, _ = execute_test(final_task_dir, timeout=15)
                            is_killed = (m_ret != 0)
                            if is_killed: killed_count += 1
                            status = "KILLED" if is_killed else "SURVIVED"
                            if m_ret == -999: status = "TIMEOUT_KILLED"
                            mutants_log.append({
                                "id": f"m_{idx}", "operator": m.get('operator'),
                                "status": status, "killed": is_killed
                            })
                    finally:
                        shutil.move(solution_path + ".bak", solution_path)
                    
                    mutation_stats["killed"] = killed_count
                    mutation_stats["score"] = (killed_count / len(mutants)) * 100
                    print(f"🎯 Score: {mutation_stats['score']:.1f}%")

            # 保存 mutants.json
            with open(os.path.join(final_task_dir, "mutants.json"), "w", encoding='utf-8') as f:
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

        with open(REPORT_FILE, 'w') as f: json.dump(final_report, f, indent=2)

    passed_cnt = sum(1 for r in final_report if r['source_check']['passed'])
    valid_scores = [r['mutation_check']['score'] for r in final_report if r['source_check']['passed'] and r['mutation_check']['score'] is not None]
    avg_score = sum(valid_scores)/len(valid_scores) if valid_scores else 0
    
    print("\n" + "="*40)
    print(f"REPORT SUMMARY (Pass@{N_SAMPLES} + Anti-Truncation)")
    print(f"Pass Rate: {passed_cnt}/{len(final_report)}")
    print(f"Avg Mutation Score: {avg_score:.2f}%")
    print("="*40)

if __name__ == "__main__":
    main()