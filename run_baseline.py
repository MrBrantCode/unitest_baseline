#第一版，保留了生成变异代码的逻辑
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
MODEL_PATH = "./model/CodeRM-8B"
BASE_OUTPUT_DIR = "./mut_cp"
REPORT_DIR = "./results"
REPORT_FILE = os.path.join(REPORT_DIR, "final_report.json")

BATCH_SIZE = 10 

# ================= 1. 全功能变异引擎 (FullMutator) =================
# (为了节省篇幅，这里保持之前的变异引擎代码不变，请务必保留！)
class FullMutator(ast.NodeTransformer):
    def __init__(self):
        self.mutants = []
        self.current_source = ""
    def gen_mutants(self, source_code):
        self.current_source = source_code
        self.mutants = []
        try:
            tree = ast.parse(source_code)
        except SyntaxError:
            return []
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp): self._mutate_binop(tree, node)
            elif isinstance(node, ast.Compare): self._mutate_compare(tree, node)
            elif isinstance(node, ast.BoolOp): self._mutate_boolop(tree, node)
            elif isinstance(node, ast.AugAssign): self._mutate_aug_assign(tree, node)
            elif isinstance(node, ast.Constant): self._mutate_constant(tree, node)
            elif isinstance(node, ast.UnaryOp): self._mutate_unaryop(tree, node)
        return self.mutants
    def _save_mutation(self, t, n, v, a, o):
        old = getattr(n, a)
        setattr(n, a, v)
        try:
            c = self._unparse(t)
            if c != self.current_source:
                self.mutants.append({"operator": o, "lineno": getattr(n, 'lineno', -1), "code": c})
        except: pass
        finally: setattr(n, a, old)
    def _mutate_binop(self, t, n):
        map_ops = {ast.Add: [ast.Sub(), ast.Mult()], ast.Sub: [ast.Add()], ast.Mult: [ast.Div(), ast.Add()], ast.Div: [ast.Mult()], ast.Mod: [ast.Mult()], ast.Pow: [ast.Mult()]}
        if type(n.op) in map_ops: [self._save_mutation(t, n, op, 'op', 'AOR') for op in map_ops[type(n.op)]]
    def _mutate_compare(self, t, n):
        if not n.ops: return
        map_ops = {ast.Eq: [ast.NotEq()], ast.NotEq: [ast.Eq()], ast.Lt: [ast.LtE(), ast.GtE()], ast.LtE: [ast.Lt(), ast.Gt()], ast.Gt: [ast.GtE(), ast.LtE()], ast.GtE: [ast.Gt(), ast.Lt()]}
        if type(n.ops[0]) in map_ops: [self._save_mutation(t, n, [op] + n.ops[1:], 'ops', 'ROR') for op in map_ops[type(n.ops[0])]]
    def _mutate_boolop(self, t, n):
        map_ops = {ast.And: [ast.Or()], ast.Or: [ast.And()]}
        if type(n.op) in map_ops: [self._save_mutation(t, n, op, 'op', 'LCR') for op in map_ops[type(n.op)]]
    def _mutate_aug_assign(self, t, n):
        map_ops = {ast.Add: [ast.Sub()], ast.Sub: [ast.Add()], ast.Mult: [ast.Div()]}
        if type(n.op) in map_ops: [self._save_mutation(t, n, op, 'op', 'ASR') for op in map_ops[type(n.op)]]
    def _mutate_unaryop(self, t, n):
        map_ops = {ast.USub: [ast.UAdd()], ast.UAdd: [ast.USub()]}
        if type(n.op) in map_ops: [self._save_mutation(t, n, op, 'op', 'UOI') for op in map_ops[type(n.op)]]
    def _mutate_constant(self, t, n):
        v = n.value; cands = []
        if isinstance(v, bool): cands.append(not v)
        elif isinstance(v, (int, float)): cands.extend([v+1, v-1]); cands.append(0) if v!=0 else None; cands.append(1) if v!=1 else None
        elif isinstance(v, str): cands.append("" if v else "MUT")
        for c in cands: self._save_mutation(t, n, c, 'value', 'CRP')
    def _unparse(self, t):
        if sys.version_info >= (3, 9): return ast.unparse(t)
        import astunparse; return astunparse.unparse(t).strip()

# ================= 2. 工具函数 (关键修复) =================

def clean_output(text):
    """
    清洗代码：掐头去尾
    """
    # 1. 去除 Markdown
    text = re.sub(r'```python', '', text)
    text = re.sub(r'```', '', text)
    
    # 2. 掐头 (Head Trimming) - 修复你的问题
    # 找到 'import unittest' 的位置，丢弃前面的废话
    start_marker = "import unittest"
    idx = text.find(start_marker)
    
    if idx != -1:
        # 如果找到了，保留从 import 开始的内容
        text = text[idx:]
    else:
        # 如果没找到 import unittest，尝试找 class Test
        class_match = re.search(r'^class\s+\w+', text, re.MULTILINE)
        if class_match:
            text = "import unittest\n" + text[class_match.start():]
    
    text = text.strip()
    
    # 3. 去尾 (Tail Trimming) - 使用 AST
    try:
        tree = ast.parse(text)
        if not tree.body: return text
        
        valid_nodes = []
        for node in tree.body:
            # 移除模型自己写的 main 函数，稍后统一注入
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
                # 只保留有效行
                text = '\n'.join(lines[:end_line])
                
    except SyntaxError:
        pass # 如果这里还有语法错误，说明模型生成的代码本身就是坏的，交给 Source Check 拦截
        
    return text

def setup_task_env(task_id, solution_code, question_text, test_code, entry_point):
    """初始化环境"""
    task_dir = os.path.join(BASE_OUTPUT_DIR, task_id)
    os.makedirs(task_dir, exist_ok=True)
    
    # 1. 写入源码
    with open(os.path.join(task_dir, "solution.py"), "w", encoding='utf-8') as f:
        f.write(f'"""\nORIGINAL QUESTION:\n{question_text}\n"""\n\n{solution_code}')
        
    # 2. 写入测试代码
    lines = test_code.split('\n')
    cleaned_lines = [l for l in lines if not re.match(r'^from\s+solution\s+import', l.strip())]
    
    final_test_code = f"from solution import {entry_point}\n" + "\n".join(cleaned_lines)
    
    # 3. 强制注入 Main
    final_test_code += "\n\nif __name__ == '__main__':\n    unittest.main()\n"

    with open(os.path.join(task_dir, "test_suite.py"), "w", encoding='utf-8') as f:
        f.write(final_test_code)
    
    return task_dir

def execute_test(task_dir, timeout=5):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = task_dir + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(
            ["python3", "test_suite.py"], cwd=task_dir, capture_output=True, text=True, env=env, timeout=timeout
        )
        combined_output = result.stderr + "\n" + result.stdout
        return result.returncode, combined_output
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"
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

# ================= 3. 主流程 =================

def main():
    if os.path.exists(BASE_OUTPUT_DIR): shutil.rmtree(BASE_OUTPUT_DIR)
    os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)

    with open(DATA_PATH, 'r') as f:
        all_data = [json.loads(line) for line in f if line.strip()]
    
    print(f"🚀 Loading CodeRM-8B...")
    llm = LLM(model=MODEL_PATH, tensor_parallel_size=2, dtype="bfloat16")
    sampling_params = SamplingParams(temperature=0.2, max_tokens=2048, stop=["<|end_of_text|>"])

    final_report = []
    mutator = FullMutator()

    print(f"\n🚀 Starting Baseline Evaluation...")

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
        outputs = llm.generate(prompts, sampling_params)
        
        for j, output in enumerate(outputs):
            item = batch[j]
            task_id = item['task_id']
            solution_code = item['canonical_solution']
            
            # Setup (这里会调用修复后的 clean_output)
            test_code = clean_output(output.outputs[0].text)
            task_dir = setup_task_env(
                task_id, solution_code, item.get('original_question', ''), test_code, item['entry_point']
            )
            
            # 1. Gen Mutants
            mutants = mutator.gen_mutants(solution_code)
            print(f"  Task {task_id}: Gen {len(mutants)} muts. ", end="", flush=True)
            
            # 2. Run Source
            ret_code, output_log = execute_test(task_dir)
            pass_source = (ret_code == 0)
            
            run_n, fail_n, err_n = parse_unittest_summary(output_log)
            failed_total = fail_n + err_n
            
            source_check_info = {
                "passed": pass_source,
                "return_code": ret_code,
                "stats": {"run": run_n, "failed": failed_total},
                "failed_cases": extract_failed_tests(output_log),
                "log_snippet": output_log[-500:] if output_log else ""
            }
            
            mutants_log = []
            mutation_stats = {"killed": 0, "total": len(mutants), "score": None}

            if not pass_source:
                if run_n > 0: print(f"❌ Source Fail ({failed_total}/{run_n} failed).")
                else: print(f"❌ Source Fail (Crash/Syntax Error).")
                for idx, m in enumerate(mutants):
                    mutants_log.append({
                        "id": f"m_{idx}", "operator": m['operator'], "lineno": m['lineno'],
                        "status": "SKIPPED_SOURCE_FAIL", "mutated_code": m['code']
                    })
            else:
                print("✅ Source Pass.", end=" ", flush=True)
                if len(mutants) == 0:
                    print("⚠️ No mutants.")
                    mutation_stats["score"] = None
                else:
                    print("Testing mutants...", end="", flush=True)
                    killed_count = 0
                    solution_path = os.path.join(task_dir, "solution.py")
                    shutil.copy(solution_path, solution_path + ".bak")
                    try:
                        for idx, m in enumerate(mutants):
                            with open(solution_path, "w", encoding='utf-8') as f: f.write(m['code'])
                            m_ret, _ = execute_test(task_dir, timeout=2)
                            is_killed = (m_ret != 0)
                            if is_killed: killed_count += 1
                            mutants_log.append({
                                "id": f"m_{idx}", "operator": m['operator'], 
                                "status": "KILLED" if is_killed else "SURVIVED",
                                "mutated_code": m['code']
                            })
                    finally:
                        shutil.move(solution_path + ".bak", solution_path)
                    
                    mutation_stats["killed"] = killed_count
                    mutation_stats["score"] = (killed_count / len(mutants)) * 100
                    print(f"🎯 Score: {mutation_stats['score']:.1f}%")

            with open(os.path.join(task_dir, "mutants.json"), "w", encoding='utf-8') as f:
                json.dump({
                    "task_id": task_id, 
                    "source_check": source_check_info,
                    "mutation_stats": mutation_stats, 
                    "mutants": mutants_log
                }, f, indent=2)

            final_report.append({
                "task_id": task_id, "source_check": source_check_info, "mutation_check": mutation_stats
            })

        with open(REPORT_FILE, 'w') as f: json.dump(final_report, f, indent=2)

    valid_scores = [r['mutation_check']['score'] for r in final_report if r['source_check']['passed'] and r['mutation_check']['score'] is not None]
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