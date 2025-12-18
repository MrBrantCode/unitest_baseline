import os
import subprocess
import tempfile
import sys

# 手动构造一个简单的案例（取自你的报错日志 task_id: taco_14278）
CODE = """
def equal_sigma1(nMax):
    cache = {}
    def sum_div(x):
        if x not in cache:
            cache[x] = sum((i for i in range(1, x + 1) if x % i == 0))
        return cache[x]
    def is_required(x):
        reversed_x = int(str(x)[::-1])
        return x != reversed_x and sum_div(x) == sum_div(reversed_x)
    required = [x for x in range(1, nMax + 1) if is_required(x)]
    return sum((x for x in required if x <= nMax))
"""

TEST = """
import unittest
# 注意：这里我们模拟脚本里的注入行为，稍后在文件里写入
class TestEqualSigma1(unittest.TestCase):
    def test_equal_sigma1(self):
        self.assertEqual(equal_sigma1(10), 19)
"""

ENTRY_POINT = "equal_sigma1"

def debug_run():
    print("🚀 Starting Debug Run...")
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"📂 Temp Dir: {temp_dir}")
        
        src_path = os.path.join(temp_dir, "solution.py")
        test_path = os.path.join(temp_dir, "test_solution.py")
        
        # 1. 写入 solution.py
        with open(src_path, 'w') as f:
            f.write(CODE)
            
        # 2. 写入 test_solution.py (注入 import)
        test_code_fixed = f"from solution import {ENTRY_POINT}\n" + TEST
        with open(test_path, 'w') as f:
            f.write(test_code_fixed)
            
        print("✅ Files written.")

        # 3. 构造命令
        # 尝试直接调用 mut.py，如果不成，尝试 python -m mutpy (虽然 mutpy 不支持 -m，但我们要确认环境)
        cmd = ["mut.py", "--target", "solution", "--unit-test", "test_solution", "--runner", "unittest"]
        
        print(f"🏃 Running command: {' '.join(cmd)}")
        
        # 4. 运行并捕获所有输出
        try:
            # 关键：把 PYTHONPATH 设为当前临时目录，确保能 import solution
            env = os.environ.copy()
            env["PYTHONPATH"] = temp_dir + os.pathsep + env.get("PYTHONPATH", "")

            result = subprocess.run(
                cmd, 
                cwd=temp_dir, 
                capture_output=True, 
                text=True, 
                env=env, # 注入环境变量
                timeout=30
            )
            
            print("\n--- STDOUT ---")
            print(result.stdout)
            print("\n--- STDERR ---")
            print(result.stderr)
            print(f"\nReturn Code: {result.returncode}")
            
        except FileNotFoundError:
            print("\n❌ Error: 'mut.py' command not found! Did you run `pip install mutpy-x`?")
            print("Try running: pip show mutpy-x")
        except Exception as e:
            print(f"\n❌ Execution Exception: {e}")

if __name__ == "__main__":
    debug_run()