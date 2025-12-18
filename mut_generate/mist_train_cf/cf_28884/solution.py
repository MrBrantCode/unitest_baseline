"""
QUESTION:
Write a function `max_non_adjacent_sum` that takes a list of integers as input and returns the maximum sum of non-adjacent numbers. The input list will contain at least one element.
"""

from typing import List

def max_non_adjacent_sum(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(0, max(nums))

    max_sum = [0] * len(nums)
    max_sum[0] = max(0, nums[0])
    max_sum[1] = max(max_sum[0], nums[1])

    for i in range(2, len(nums)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2] + nums[i])

    return max_sum[-1]