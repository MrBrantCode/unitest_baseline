"""
QUESTION:
Write a function `min_half_or_unique` that takes a list of integers `nums` as input, where 1 <= len(nums) <= 1000. The function should return the minimum of two values: half the length of `nums` and the number of unique elements in `nums`, rounded down to the nearest integer.
"""

def min_half_or_unique(nums):
    half = len(nums) / 2
    unique_nums = list(set(nums))
    unique_count = len(unique_nums)
    return int(min(half, unique_count))