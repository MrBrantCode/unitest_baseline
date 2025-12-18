"""
QUESTION:
Write a function `max_difference` that takes a list of integers as input and returns the maximum difference between any two numbers in the list. If the list contains less than two elements, the function should return 0.
"""

from typing import List

def max_difference(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0
    min_num = nums[0]
    max_diff = 0
    for num in nums:
        max_diff = max(max_diff, num - min_num)
        min_num = min(min_num, num)
    return max_diff