"""
QUESTION:
Write a function `max_sum_subarray` that takes in a list of integers `num` with at least 12 elements, where elements can be positive, negative, or zero, and returns the maximum sum of a subarray that is at least 12 elements long.
"""

from typing import List

def max_sum_subarray(nums: List[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums) - 11):
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if j - i >= 11:
                max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
    return max_sum