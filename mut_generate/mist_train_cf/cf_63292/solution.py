"""
QUESTION:
Design a function named `median_in_range` that takes a list of integers `l`, a lower limit `lower_limit`, and an upper limit `upper_limit`. The function should return `True` if the median of `l` falls within the range defined by `lower_limit` and `upper_limit`, inclusive, and `False` otherwise. The function should handle both even and odd length lists, and it should not modify the original list.
"""

def median_in_range(nums: list, lower_limit: int, upper_limit: int) -> bool:
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    median = sorted_nums[n//2] if n % 2 else (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2

    return lower_limit <= median <= upper_limit