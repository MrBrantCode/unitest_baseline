# 读取./datasets/CodeRM-filter/mist_test_cf.jsonl，生成变异体，并保存为./mut_generate/task_id/mutants.json
import json
import os
import shutil
import ast
import sys
import copy
import warnings
import difflib
try:
    from tqdm import tqdm
except ModuleNotFoundError:
    # 兼容：如果环境里没装 tqdm，就降级为普通迭代（不影响功能，只是没有进度条）
    def tqdm(iterable, **kwargs):
        return iterable

# ================= 1. 全功能变异引擎 (0依赖) =================

class FullMutator(ast.NodeTransformer):
    """
    全功能变异器，支持 AOR, ROR, LCR, CRP, UOI 等标准算子。
    """
    def __init__(self):
        self.mutants = []
        self.current_source = ""

    def gen_mutants(self, source_code):
        self.current_source = source_code
        self.mutants = []
        
        try:
            # 某些数据集中会出现字符串里包含反斜杠但未写成 raw string 的情况，
            # Python 在 parse/compile 时会打印大量 SyntaxWarning（不影响功能但会刷屏）。
            # 这里统一屏蔽，避免批量生成时日志污染。
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", SyntaxWarning)
                tree = ast.parse(source_code)
        except SyntaxError:
            return []

        # 遍历树中的每一个节点
        for node in ast.walk(tree):
            
            # 1. 二元运算 (AOR): +, -, *, /, %, ...
            if isinstance(node, ast.BinOp):
                self._mutate_binop(tree, node)
            
            # 2. 比较运算 (ROR): ==, !=, <, <=, >, >=
            elif isinstance(node, ast.Compare):
                self._mutate_compare(tree, node)
                
            # 3. 逻辑运算 (LCR): and, or
            elif isinstance(node, ast.BoolOp):
                self._mutate_boolop(tree, node)
            
            # 4. 增强赋值 (ASR): +=, -=, *=
            elif isinstance(node, ast.AugAssign):
                self._mutate_aug_assign(tree, node)

            # 5. 常量替换 (CRP): 数字, 字符串, 布尔
            elif isinstance(node, ast.Constant):
                self._mutate_constant(tree, node)
                
            # 6. 一元运算 (UOI): not, -, +
            elif isinstance(node, ast.UnaryOp):
                self._mutate_unaryop(tree, node)

        return self.mutants

    def _save_mutation(self, original_tree, node, new_attr_val, attr_name, op_code):
        """通用保存逻辑: 替换属性 -> 生成代码 -> 恢复属性"""
        old_val = getattr(node, attr_name)
        setattr(node, attr_name, new_attr_val)
        
        try:
            mutated_code = self._unparse(original_tree)
            # 只有当代码真正改变时才保存
            if mutated_code != self.current_source:
                lineno = getattr(node, 'lineno', -1)
                self.mutants.append({
                    "operator": op_code,
                    "lineno": lineno,
                    "original_line": self._get_line(lineno),
                    # 便于快速对比：变异后该行长什么样（避免你去翻很长的 code 字段）
                    # 说明：ast.unparse 可能导致行号整体偏移（例如把表达式换行/合并空行），
                    # 所以这里用 diff 做“原始行号 -> 变异后行号”的映射，避免取错行（例如误取到 end += 1）。
                    "mutated_line": self._get_mutated_line(mutated_code, lineno),
                    "code": mutated_code
                })
        except Exception:
            pass
        finally:
            # 恢复现场，保证AST不被破坏，继续下一个变异
            setattr(node, attr_name, old_val)

    def _mutate_binop(self, tree, node):
        """Arithmetic Operator Replacement (AOR)"""
        # 映射规则：左边是原操作符，右边是候选替换列表
        map_ops = {
            ast.Add: [ast.Sub(), ast.Mult()],           # + -> -, *
            ast.Sub: [ast.Add(), ast.Mult()],           # - -> +, *
            ast.Mult: [ast.Div(), ast.Add(), ast.Pow()],# * -> /, +, **
            ast.Div: [ast.Mult(), ast.FloorDiv()],      # / -> *, //
            ast.FloorDiv: [ast.Div(), ast.Mult()],      # // -> /, *
            ast.Mod: [ast.Mult(), ast.Add()],           # % -> *, +
            ast.Pow: [ast.Mult(), ast.Add()],           # ** -> *, +
            ast.BitAnd: [ast.BitOr()],                  # & -> |
            ast.BitOr: [ast.BitAnd(), ast.BitXor()],    # | -> &, ^
            ast.BitXor: [ast.BitOr()]                   # ^ -> |
        }
        curr_type = type(node.op)
        if curr_type in map_ops:
            for new_op in map_ops[curr_type]:
                self._save_mutation(tree, node, new_op, 'op', 'AOR')

    def _mutate_compare(self, tree, node):
        """Relational Operator Replacement (ROR)"""
        # 注意：Python 支持 a < b < c，ops 是一个列表。
        # 为了简单且稳健，我们只变异第一个操作符，覆盖绝大多数情况。
        if not node.ops: return
        
        # 针对第一个比较符进行变异
        curr_op = node.ops[0]
        curr_type = type(curr_op)
        
        # 核心逻辑：这里定义了如何挑选更刁钻的变异
        map_ops = {
            ast.Eq:    [ast.NotEq()],                     # == -> !=
            ast.NotEq: [ast.Eq()],                        # != -> ==
            ast.Lt:    [ast.LtE(), ast.GtE(), ast.NotEq()], # <  -> <=, >=, != (边界测试!)
            ast.LtE:   [ast.Lt(), ast.Gt(), ast.Eq()],      # <= -> <, >, ==
            ast.Gt:    [ast.GtE(), ast.LtE(), ast.NotEq()], # >  -> >=, <=, !=
            ast.GtE:   [ast.Gt(), ast.Lt(), ast.Eq()],      # >= -> >, <, ==
            ast.Is:    [ast.IsNot()],                     # is -> is not
            ast.IsNot: [ast.Is()],                        # is not -> is
            ast.In:    [ast.NotIn()],                     # in -> not in
            ast.NotIn: [ast.In()]                         # not in -> in
        }

        if curr_type in map_ops:
            old_ops_list = node.ops
            # 遍历每一个替换候选
            for new_op_inst in map_ops[curr_type]:
                # 构造新的 ops 列表 (只替换第一个)
                new_ops_list = [new_op_inst] + old_ops_list[1:]
                self._save_mutation(tree, node, new_ops_list, 'ops', 'ROR')

    def _mutate_boolop(self, tree, node):
        """Logical Connector Replacement (LCR)"""
        map_ops = {
            ast.And: [ast.Or()],
            ast.Or:  [ast.And()]
        }
        curr_type = type(node.op)
        if curr_type in map_ops:
            for new_op in map_ops[curr_type]:
                self._save_mutation(tree, node, new_op, 'op', 'LCR')

    def _mutate_aug_assign(self, tree, node):
        """Assignment Operator Replacement (ASR) e.g. += """
        map_ops = {
            ast.Add: [ast.Sub()],
            ast.Sub: [ast.Add()],
            ast.Mult: [ast.Div()],
            ast.Div: [ast.Mult()]
        }
        curr_type = type(node.op)
        if curr_type in map_ops:
            for new_op in map_ops[curr_type]:
                self._save_mutation(tree, node, new_op, 'op', 'ASR')

    def _mutate_unaryop(self, tree, node):
        """Unary Operator Insertion/Replacement (UOI)"""
        map_ops = {
            ast.Not: [], # not a -> a (直接去掉，逻辑比较复杂，这里暂略)
            ast.USub: [ast.UAdd()], # -a -> +a
            ast.UAdd: [ast.USub()], # +a -> -a
            ast.Invert: []
        }
        # 特殊处理：如果是 if not a，可以通过去掉 Not 来变异
        # 但 ast 结构里 remove node 比较麻烦，这里只做简单的替换
        curr_type = type(node.op)
        if curr_type in map_ops:
            for new_op in map_ops[curr_type]:
                self._save_mutation(tree, node, new_op, 'op', 'UOI')

    def _mutate_constant(self, tree, node):
        """Constant Replacement (CRP)"""
        val = node.value
        candidates = []
        
        # 1. Boolean
        if isinstance(val, bool):
            candidates.append(not val)
            
        # 2. Number (Int/Float)
        elif isinstance(val, (int, float)):
            candidates.append(val + 1)
            candidates.append(val - 1)
            if val != 0: candidates.append(0)
            if val != 1: candidates.append(1)
            if val > 0: candidates.append(-val) # 符号反转
            
        # 3. String
        elif isinstance(val, str):
            if val == "": 
                candidates.append("MUTATED")
            else:
                candidates.append("") # 空串测试
                # candidates.append(val + "_MUT") # 变脏
        
        for new_val in candidates:
            self._save_mutation(tree, node, new_val, 'value', 'CRP')

    # --- 辅助 ---
    def _unparse(self, tree):
        if sys.version_info >= (3, 9):
            return ast.unparse(tree)
        import astunparse # Py < 3.9
        return astunparse.unparse(tree).strip()

    def _get_line(self, lineno):
        if lineno == -1: return ""
        lines = self.current_source.split('\n')
        if 0 <= lineno - 1 < len(lines):
            return lines[lineno - 1].strip()
        return ""

    def _get_line_from_source(self, source, lineno):
        """从任意源码字符串中提取指定行（用于 mutated_line）"""
        if lineno == -1 or not source:
            return ""
        lines = source.split('\n')
        if 0 <= lineno - 1 < len(lines):
            return lines[lineno - 1].strip()
        return ""

    def _get_mutated_line(self, mutated_source, original_lineno):
        """
        用行级 diff 将 original_lineno 映射到 mutated_source 中的对应行，尽量保证 mutated_line 真正指向“发生变化的那一行”。
        """
        if original_lineno == -1 or not mutated_source:
            return ""

        a = self.current_source.splitlines()
        b = mutated_source.splitlines()
        i = original_lineno - 1
        if i < 0 or i >= len(a):
            return ""

        sm = difflib.SequenceMatcher(a=a, b=b)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if i1 <= i < i2:
                if tag == "equal":
                    # 行未变，但可能因为前面插入/删除导致整体偏移；做平移映射
                    j = j1 + (i - i1)
                    return b[j].strip() if 0 <= j < len(b) else ""
                if tag in ("replace", "delete"):
                    # 这一段在变异后被替换/删除；取对应的替换行（若无则空）
                    if j1 < j2:
                        j = min(j1 + (i - i1), j2 - 1)
                        return b[j].strip() if 0 <= j < len(b) else ""
                    return ""
                if tag == "insert":
                    # insert 不会覆盖 a 的行区间，理论上不会进来；兜底
                    return b[j1].strip() if 0 <= j1 < len(b) else ""

        # 兜底：直接按相同行号取（不推荐，但总比没有强）
        return self._get_line_from_source(mutated_source, original_lineno)

# ================= 2. 配置 =================
# 现在支持一次性处理 4 个数据集，并分别输出到 mut_generate/<dataset_name>/ 下。
# 例如：mut_generate/mist_test_cf/<task_id>/solution.py & mutants.json
DATASET_PATHS = [
    "./datasets/CodeRM-filter/mist_train_cf.jsonl",
    "./datasets/CodeRM-filter/mist_test_cf.jsonl",
    "./datasets/CodeRM-filter/mist_train_taco.jsonl",
    "./datasets/CodeRM-filter/mist_test_taco.jsonl",
]

OUTPUT_ROOT_DIR = "./mut_generate"
# 可选：用于快速冒烟测试/调试。默认 None 表示不限制（跑全量数据集）。
MAX_TASKS_PER_DATASET = None

# ================= 3. 主流程 =================

def main():
    # 1) 清空输出根目录（保证四个数据集输出是干净的）
    if os.path.exists(OUTPUT_ROOT_DIR):
        print(f"🧹 Clearing directory: {OUTPUT_ROOT_DIR}")
        shutil.rmtree(OUTPUT_ROOT_DIR)
    os.makedirs(OUTPUT_ROOT_DIR, exist_ok=True)

    mutator = FullMutator()

    # 2) 逐个数据集生成
    for data_path in DATASET_PATHS:
        dataset_name = os.path.splitext(os.path.basename(data_path))[0]  # e.g. mist_test_cf
        output_dir = os.path.join(OUTPUT_ROOT_DIR, dataset_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"\n📂 Loading data from {data_path} ...")
        with open(data_path, 'r', encoding='utf-8') as f:
            data = [json.loads(line) for line in f if line.strip()]

        if MAX_TASKS_PER_DATASET is not None:
            data = data[:MAX_TASKS_PER_DATASET]

        print(f"🚀 Generating mutants for {len(data)} tasks (dataset={dataset_name}, Engine: Full-Spectrum)...")

        stats = {
            "dataset": dataset_name,
            "data_path": data_path,
            "total_tasks": len(data),
            "zero_mutants_tasks": [],
            "total_mutants_generated": 0,
            "operator_stats": {}  # 统计每种算子生成了多少个
        }

        for item in tqdm(data, desc=f"[{dataset_name}]"):
            task_id = item['task_id']
            code = item['canonical_solution']
            question = item.get('original_question', 'No question.')
            entry_point = item['entry_point']

            # 3. 创建目录：mut_generate/<dataset_name>/<task_id>/
            task_dir = os.path.join(output_dir, task_id)
            os.makedirs(task_dir, exist_ok=True)

            # 4. 写入源码
            solution_path = os.path.join(task_dir, "solution.py")
            content = f'"""\nQUESTION:\n{question}\n"""\n\n{code}'
            with open(solution_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # 5. 生成变异体
            mutants = mutator.gen_mutants(code)

            # 统计
            stats["total_mutants_generated"] += len(mutants)
            if len(mutants) == 0:
                stats["zero_mutants_tasks"].append(task_id)

            for m in mutants:
                op = m['operator']
                stats['operator_stats'][op] = stats['operator_stats'].get(op, 0) + 1

            # 6. 写入 mutants.json
            mutants_data = {
                "task_id": task_id,
                "entry_point": entry_point,
                "mutant_count": len(mutants),
                "mutants": mutants
            }

            with open(os.path.join(task_dir, "mutants.json"), 'w', encoding='utf-8') as f:
                json.dump(mutants_data, f, indent=2, ensure_ascii=False)

        # ================= 单数据集报告 =================
        print("\n" + "="*40)
        print(f"MUTATION GENERATION REPORT ({dataset_name})")
        print(f"Data Path: {data_path}")
        print(f"Total Tasks: {stats['total_tasks']}")
        print(f"Total Mutants Generated: {stats['total_mutants_generated']}")
        print(f"Tasks with 0 mutants: {len(stats['zero_mutants_tasks'])}")
        print("\n--- Operator Distribution ---")
        for op, count in sorted(stats['operator_stats'].items(), key=lambda x: x[0]):
            print(f"  {op}: {count}")
        print(f"\nOutput Directory: {output_dir}")
        print("="*40)

if __name__ == "__main__":
    main()