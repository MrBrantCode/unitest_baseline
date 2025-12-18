# 用于将CodeRM-UnitTest数据集拆分为训练集和测试集，并保存为jsonl格式
import pandas as pd
import json
import ast
import os
import random
from tqdm import tqdm

# ================= 配置路径 =================
BASE_DIR = "datasets"
SOURCE_DIR = os.path.join(BASE_DIR, "CodeRM-UnitTest")
OUTPUT_DIR = os.path.join(BASE_DIR, "CodeRM-filter")

# 输入文件路径
FILE_CF = os.path.join(SOURCE_DIR, "unit_test_codefeedback-filter.parquet")
FILE_TACO = os.path.join(SOURCE_DIR, "unit_test_taco-train.parquet")

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================= 辅助函数 =================

def get_function_name(code):
    """提取入口函数名"""
    try:
        tree = ast.parse(code)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                return node.name
    except:
        return None
    return None

def is_code_clean(code):
    """
    过滤逻辑：
    1. 代码行数 > 60 则剔除 (RL计算成本控制)
    2. 剔除危险依赖 (requests, socket等)
    """
    if len(code.split('\n')) > 60: 
        return False
    
    forbidden_keywords = [
        'import requests', 'import socket', 'import threading', 
        'subprocess', 'open(', 'sys.stdin'
    ]
    if any(k in code for k in forbidden_keywords):
        return False
        
    return True

def process_and_save(source_name, input_path):
    """
    处理单个数据集并保存为 Train/Test 两个文件
    """
    print(f"\n🚀 Processing {source_name} from: {input_path}")
    
    if not os.path.exists(input_path):
        print(f"❌ Error: File not found: {input_path}")
        return

    # 1. 读取数据
    df = pd.read_parquet(input_path)
    processed_items = []
    
    # 2. 清洗与提取
    # 使用前缀区分 ID，例如 "cf_0", "taco_0"
    prefix = "cf" if "codefeedback" in source_name.lower() else "taco"
    
    for idx, row in tqdm(df.iterrows(), total=len(df), desc=f"Cleaning {source_name}"):
        code = row['code_ground_truth']
        
        # 过滤
        if not is_code_clean(code):
            continue
            
        entry_point = get_function_name(code)
        if not entry_point:
            continue
            
        # 构建数据
        item = {
            "task_id": f"{prefix}_{row['task_id']}",
            "prompt": code,  # RL 输入
            "entry_point": entry_point,
            "canonical_solution": code, # Ground Truth
            "original_question": row.get('question', '')
        }
        processed_items.append(item)

    print(f"📊 Stats for {source_name}: Raw {len(df)} -> Valid {len(processed_items)}")

    # 3. 打乱与切分
    random.seed(42)
    random.shuffle(processed_items)

    test_size = 100
    if len(processed_items) > test_size:
        test_data = processed_items[:test_size]
        train_data = processed_items[test_size:]
    else:
        # 极少情况做兜底
        test_data = processed_items
        train_data = []

    # 4. 定义输出文件名
    train_file = os.path.join(OUTPUT_DIR, f"mist_train_{prefix}.jsonl")
    test_file = os.path.join(OUTPUT_DIR, f"mist_test_{prefix}.jsonl")

    # 5. 写入文件
    print(f"💾 Saving to {OUTPUT_DIR}...")
    
    with open(train_file, 'w', encoding='utf-8') as f:
        for item in train_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    with open(test_file, 'w', encoding='utf-8') as f:
        for item in test_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

    print(f"✅ {source_name} Done:")
    print(f"   - Train: {len(train_data)} samples -> {os.path.basename(train_file)}")
    print(f"   - Test:  {len(test_data)} samples  -> {os.path.basename(test_file)}")

# ================= 主执行流程 =================

def main():
    # 处理 CodeFeedback
    process_and_save("CodeFeedback", FILE_CF)
    
    # 处理 TACO
    process_and_save("TACO", FILE_TACO)

if __name__ == "__main__":
    main()