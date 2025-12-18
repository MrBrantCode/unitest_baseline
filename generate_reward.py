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
N_SAMPLES = 3  # Pass@3

# === MIST 奖励超参数 ===
ALPHA_QUAL = 0.2     
RHO_PENALTY = 0.5    
GATE_PASS_REWARD = 0.5 
GATE_FAIL_PENALTY = -1.0  # Crash 时的直接负分

# ================= 1. 核心工具函数 (V7.0 斩尾版) =================

def clean_output(text):
    """
    清洗代码 V7.0
    1. 提取 Markdown 代码块。
    2. 去除头部废话。
    3. 检测到 unittest.main() 后，直接切除后面所有内容 (斩尾)。
    """
    # 1. 尝试提取 Markdown 代码块
    pattern = r'```(?:python)?\s*(.*?)```'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        text = match.group(1)
    
    # 2. 简单的行级过滤：找到第一行像代码的地方开始
    lines = text.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith(('import ', 'from ', 'class ', 'def ', '@', '#')):
            start_idx = i
            break
    text = '\n'.join(lines[start_idx:])
    
    # 3. 斩尾逻辑
    if "unittest.main()" in text:
        lines = text.split('\n')
        cut_idx = -1
        for i, line in enumerate(lines):
            if "unittest.main()" in line:
                cut_idx = i
                break
        
        if cut_idx != -1:
            text = '\n'.join(lines[:cut_idx+1])

    text = text.strip()

    # 4. 补充 import unittest
    if "import unittest" not in text:
        text = "import unittest\n" + text

    return text

def setup_task_env(task_id, solution_code, question_text, test_code, entry_point):
    task_dir = os.path.join(BASE_OUTPUT_DIR, task_id)
    os.makedirs(task_dir, exist_ok=True)
    
    with open(os.path.join(task_dir, "solution.py"), "w", encoding='utf-8') as f:
        f.write(f'"""\nORIGINAL QUESTION:\n{question_text}\n"""\n\n{solution_code}')
    
    lines = test_code.split('\n')
    cleaned_lines = [l for l in lines if not re.match(r'^from\s+solution\s+import', l.strip())]
    
    final_test_code = f"from solution import {entry_point}\n" + "\n".join(cleaned_lines)
    
    # 只有当 clean_output 没找到 main 时，我们才补一个
    if "unittest.main()" not in final_test_code:
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

def execute_test(task_dir, timeout, test_method=None):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = task_dir + os.pathsep + env.get("PYTHONPATH", "")
        cmd = ["python3", "test_suite.py"]
        if test_method:
            cmd = ["python3", "-m", "unittest", f"test_suite.{test_method}"]
        
        result = subprocess.run(cmd, cwd=task_dir, capture_output=True, text=True, env=env, timeout=timeout)
        return result.returncode, result.stderr + "\n" + result.stdout
    except subprocess.TimeoutExpired: return -999, "TIMEOUT"
    except Exception as e: return 1, str(e)

def parse_unittest_summary(output):
    if not output: return 0, 0, 0
    run_match = re.search(r"Ran (\d+) tests", output)
    run_count = int(run_match.group(1)) if run_match else 0
    fail_count = 0
    error_count = 0
    if re.search(r"failures=(\d+)", output): fail_count = int(re.search(r"failures=(\d+)", output).group(1))
    if re.search(r"errors=(\d+)", output): error_count = int(re.search(r"errors=(\d+)", output).group(1))
    if (fail_count == 0 and error_count == 0) and "FAILED" in output: fail_count = 1 
    return run_count, fail_count, error_count

def get_crash_reason(log):
    if not log: return "Unknown"
    if "SyntaxError" in log: return "SyntaxError"
    if "IndentationError" in log: return "IndentationError"
    if "ImportError" in log: return "ImportError"
    if "NameError" in log: return "NameError"
    if "TIMEOUT" in log: return "TIMEOUT"
    lines = [l for l in log.split('\n') if l.strip()]
    if lines: return lines[-1][:30] + "..."
    return "RuntimeError"

# ================= 2. MIST Reward Calculator =================

class MISTRewardCalculator:
    def __init__(self, task_dir, mutants):
        self.task_dir = task_dir
        self.mutants = mutants 
        self.killed_history = set() 
        n_mut = len(mutants)
        if n_mut == 0: self.w_m = 0
        else: self.w_m = 1.0 + (n_mut / 100.0) 

    def parse_test_structure(self, test_code_path):
        """AST 解析"""
        with open(test_code_path, 'r', encoding='utf-8') as f: code = f.read()
        methods = [] 
        try:
            tree = ast.parse(code)
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    is_test = False
                    if "Test" in node.name: is_test = True
                    if not is_test:
                        for base in node.bases:
                            if isinstance(base, ast.Attribute) and base.attr == 'TestCase': is_test = True; break
                            if isinstance(base, ast.Name) and base.id == 'TestCase': is_test = True; break
                    if is_test:
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef) and item.name.startswith("test"):
                                methods.append({"class": node.name, "method": item.name, "node": item})
        except SyntaxError: pass
        except Exception: pass
        return methods

    def calculate_quality_score(self, method_node):
        score = 0.0
        assertions = {
            'assertEqual': 1.0, 'assertTrue': 0.5, 'assertFalse': 0.5, 
            'assertRaises': 1.5, 'assertIn': 1.0, 'assertListEqual': 1.2
        }
        for node in ast.walk(method_node):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                name = node.func.attr
                if name in assertions: score += assertions[name]
        return min(score, 5.0) 

    def compute_rewards(self):
        rewards_breakdown = []
        test_path = os.path.join(self.task_dir, "test_suite.py")
        
        # 1. 确定分母 (AST)
        methods = self.parse_test_structure(test_path)
        
        # === 核心修改：Crash 熔断机制 ===
        # 如果没有合法的测试方法（语法错误 或 没写类），直接返回负分
        # 不再进行任何后续计算
        if not methods:
            return GATE_FAIL_PENALTY, [{"method_name": "GLOBAL", "score": GATE_FAIL_PENALTY, "reason": "Crash/No Valid Tests"}], 0, 0

        # 2. 预筛选
        solution_path = os.path.join(self.task_dir, "solution.py")
        shutil.copy(solution_path, solution_path + ".bak")
        vulnerable_mutants = []
        try:
            for idx, m in enumerate(self.mutants):
                with open(solution_path, "w", encoding='utf-8') as f: f.write(m['code'])
                ret, _ = execute_test(self.task_dir, timeout=2)
                if ret != 0: vulnerable_mutants.append((idx, m))
        finally:
            shutil.move(solution_path + ".bak", solution_path)

        total_suite_reward = 0.0
        passed_source_count = 0 
        
        # 3. 逐个方法评估
        for meta in methods:
            full_method_name = f"{meta['class']}.{meta['method']}"
            step_info = {
                "method_name": meta['method'],
                "r_gate": 0.0, "r_qual": 0.0, "r_inc": 0.0, "total_step_score": 0.0,
                "newly_killed_ids": []
            }
            
            # Step 1: Gate Check
            ret, _ = execute_test(self.task_dir, timeout=5, test_method=full_method_name)
            
            if ret != 0:
                step_info["r_gate"] = GATE_FAIL_PENALTY
                step_info["total_step_score"] = GATE_FAIL_PENALTY
                rewards_breakdown.append(step_info)
                total_suite_reward += GATE_FAIL_PENALTY
                continue 
            
            passed_source_count += 1
            step_info["r_gate"] = GATE_PASS_REWARD
            step_info["r_qual"] = ALPHA_QUAL * self.calculate_quality_score(meta['node'])
            
            potential_targets = [t for t in vulnerable_mutants if t[0] not in self.killed_history]
            new_kills = []
            
            if potential_targets:
                shutil.copy(solution_path, solution_path + ".bak")
                try:
                    for m_idx, m_data in potential_targets:
                        with open(solution_path, "w", encoding='utf-8') as f: f.write(m_data['code'])
                        m_ret, _ = execute_test(self.task_dir, timeout=1, test_method=full_method_name)
                        if m_ret != 0: new_kills.append(m_idx)
                finally:
                    shutil.move(solution_path + ".bak", solution_path)
            
            step_info["newly_killed_ids"] = new_kills
            
            if len(new_kills) > 0:
                step_info["r_inc"] = len(new_kills) * self.w_m
                self.killed_history.update(new_kills)
            else:
                step_info["r_inc"] = -RHO_PENALTY
            
            step_total = step_info["r_gate"] + step_info["r_qual"] + step_info["r_inc"]
            step_info["total_step_score"] = round(step_total, 4)
            total_suite_reward += step_total
            rewards_breakdown.append(step_info)
        
        return total_suite_reward, rewards_breakdown, passed_source_count, len(methods)

# ================= 3. 主流程 =================

def main():
    if os.path.exists(BASE_OUTPUT_DIR): shutil.rmtree(BASE_OUTPUT_DIR)
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    if not os.path.exists(MUTANT_SOURCE_DIR):
        print("❌ Error: Mutant source directory not found.")
        return

    with open(DATA_PATH, 'r') as f:
        all_data = [json.loads(line) for line in f if line.strip()]
    
    print(f"🚀 Loading CodeRM-8B...")
    llm = LLM(model=MODEL_PATH, tensor_parallel_size=2, dtype="bfloat16", max_model_len=8192)
    
    # === 优化: 缩短 Max Tokens 到 2048 ===
    sampling_params = SamplingParams(n=N_SAMPLES, temperature=0.5, max_tokens=2048, repetition_penalty=1.05, stop=["<|end_of_text|>"])

    final_report = []

    header = f"| {'Task ID':<12} | {'Status':<10} | {'Details (Src / Mut / Score)':<65} |"
    print("\n" + "="*len(header))
    print(header)
    print("="*len(header))

    pbar = tqdm(total=len(all_data), unit="task", desc="Processing")

    for i in range(0, len(all_data), BATCH_SIZE):
        batch = all_data[i : i + BATCH_SIZE]
        prompts = [
            (f"Below is a question and it's corresponding code answer. "
             f"Please write test cases to check the correctness of the code answer. "
             f"You need to use the unittest library in Python and create a test class for testing.\n\n"
             f"### question\n{item.get('original_question', '')}\n\n"
             f"### code solution\n{item['canonical_solution']}\n\n"
             f"Please add detailed comments.")
            for item in batch
        ]
        
        outputs = llm.generate(prompts, sampling_params, use_tqdm=False) 
        
        for j, output in enumerate(outputs):
            item = batch[j]
            task_id = item['task_id']
            solution_code = item['canonical_solution']
            mutants = load_mutants_from_disk(task_id)
            
            candidates = []
            
            for candidate_idx, candidate_output in enumerate(output.outputs):
                test_code = clean_output(candidate_output.text)
                task_dir = setup_task_env(task_id, solution_code, item.get('original_question', ''), test_code, item['entry_point'])
                ret_code, output_log = execute_test(task_dir, timeout=60)
                
                run_n, fail_n, err_n = parse_unittest_summary(output_log)
                is_runnable = (run_n > 0)
                is_fully_pass = (is_runnable and fail_n == 0 and err_n == 0)
                
                candidates.append({
                    "idx": candidate_idx,
                    "is_runnable": is_runnable,
                    "is_fully_pass": is_fully_pass,
                    "task_dir": task_dir,
                    "output_log": output_log
                })

            best_candidate = candidates[0]
            perfects = [c for c in candidates if c['is_fully_pass']]
            if perfects: best_candidate = perfects[0]
            else:
                runnables = [c for c in candidates if c['is_runnable']]
                if runnables: best_candidate = runnables[0]
            
            final_task_dir = best_candidate['task_dir']
            final_log = best_candidate['output_log']
            
            mist_score = 0.0
            rewards_breakdown = []
            src_passed_count = 0
            src_total_count = 0
            
            calculator = MISTRewardCalculator(final_task_dir, mutants)
            # 计算得分 (Crash时会直接返回负分并退出)
            mist_score, rewards_breakdown, src_passed_count, src_total_count = calculator.compute_rewards()
            
            if src_total_count > 0:
                status_icon = "✅ Run"
            else:
                status_icon = "❌ Crash"
                # 确保 Crash 时的分数是负的
                mist_score = GATE_FAIL_PENALTY
                src_passed_count = 0
                src_total_count = 0

            killed_ids_final = set()
            for step in rewards_breakdown:
                if "newly_killed_ids" in step: killed_ids_final.update(step["newly_killed_ids"])
            killed_count = len(killed_ids_final)
            total_mutants = len(mutants)
            mut_rate = (killed_count / total_mutants * 100) if total_mutants > 0 else 0.0

            if status_icon == "✅ Run":
                details = f"Src: {src_passed_count}/{src_total_count}    Mut: {killed_count}/{total_mutants} ({mut_rate:.0f}%)    Score: {mist_score:.1f}"
            else:
                reason = get_crash_reason(final_log)
                details = f"Fail: {reason} (Score: {mist_score})"
            
            tqdm.write(f"| {task_id:<12} | {status_icon:<10} | {details:<65} |")

            with open(os.path.join(final_task_dir, "rewards.json"), "w", encoding='utf-8') as f:
                json.dump({
                    "task_id": task_id,
                    "total_score": round(mist_score, 4),
                    "test_suite_breakdown": rewards_breakdown
                }, f, indent=2)

            source_info = {
                "runnable": (status_icon == "✅ Run"),
                "score": mist_score,
                "stats": {"ast_total": src_total_count, "passed": src_passed_count},
                "log_snippet": final_log[-300:] if final_log else ""
            }
            mutation_stats = {
                "killed": killed_count,
                "total": total_mutants,
                "score": mut_rate
            }
            with open(os.path.join(final_task_dir, "mutants.json"), "w", encoding='utf-8') as f:
                json.dump({
                    "task_id": task_id, 
                    "source_check": source_info,
                    "mutation_stats": mutation_stats,
                }, f, indent=2)

            final_report.append({
                "task_id": task_id, 
                "runnable": (status_icon == "✅ Run"),
                "mist_score": mist_score
            })
            
            pbar.update(1)

    pbar.close()
    print("="*len(header))
    runnable_cnt = sum(1 for r in final_report if r['runnable'])
    print(f"SUMMARY: Runnable Rate (Pass/Total): {runnable_cnt}/{len(final_report)}")

if __name__ == "__main__":
    main()
