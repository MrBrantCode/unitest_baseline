# 用于删除 mut_generate 下四个数据目录里 mutant_count=0 的任务目录，并输出总删除数。
import argparse
import json
import shutil
from pathlib import Path


def should_delete_task_dir(mutants_json: Path) -> bool:
    """
    判定规则：
    - mutants.json 中 mutant_count == 0  -> 删除该 task 目录
    兼容兜底：
    - mutant_count 缺失时，如果 mutants 是空列表，也认为是 0
    """
    try:
        data = json.loads(mutants_json.read_text(encoding="utf-8"))
    except Exception:
        # 解析失败就别删，避免误伤
        return False

    mutant_count = data.get("mutant_count", None)
    if mutant_count == 0:
        return True

    mutants = data.get("mutants", None)
    if mutant_count is None and isinstance(mutants, list) and len(mutants) == 0:
        return True

    return False


def clean_dataset_dir(dataset_dir: Path, dry_run: bool = False) -> int:
    """
    清理某个数据目录（例如 mist_test_cf）下所有 task 子目录。
    返回删除的 task 目录数量。
    """
    removed = 0
    if not dataset_dir.is_dir():
        return 0

    for task_dir in dataset_dir.iterdir():
        if not task_dir.is_dir():
            continue
        mutants_json = task_dir / "mutants.json"
        if not mutants_json.exists():
            continue

        if should_delete_task_dir(mutants_json):
            removed += 1
            if dry_run:
                continue
            shutil.rmtree(task_dir, ignore_errors=True)

    return removed


def main():
    parser = argparse.ArgumentParser(
        description="删除 mut_generate 下四个数据目录里 mutant_count=0 的任务目录，并输出总删除数。"
    )
    parser.add_argument(
        "--base-dir",
        type=str,
        default=str(Path(__file__).resolve().parent),
        help="mut_generate 目录路径（默认：当前脚本所在目录）",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只统计不删除",
    )
    args = parser.parse_args()

    base_dir = Path(args.base_dir).resolve()
    if not base_dir.exists():
        print(f"❌ base_dir 不存在: {base_dir}")
        return

    # 你描述的“当前目录下的四个目录”
    # 这里按命名规则筛选，避免误扫其它文件夹
    dataset_dirs = [
        base_dir / "mist_test_cf",
        base_dir / "mist_test_taco",
        base_dir / "mist_train_cf",
        base_dir / "mist_train_taco",
    ]

    total_removed = 0
    existing_dirs = 0

    for d in dataset_dirs:
        if not d.exists():
            continue
        existing_dirs += 1
        removed = clean_dataset_dir(d, dry_run=args.dry_run)
        total_removed += removed
        print(f"{d.name}: removed {removed} task dirs")

    if existing_dirs == 0:
        print(f"❌ 未找到任何目标目录（期望在 {base_dir} 下有 mist_test_cf/mist_test_taco/mist_train_cf/mist_train_taco）")
        return

    if args.dry_run:
        print(f"\nDRY RUN: 四个目录合计将剔除 {total_removed} 个 task 目录")
    else:
        print(f"\nDONE: 四个目录合计剔除 {total_removed} 个 task 目录")


if __name__ == "__main__":
    main()

