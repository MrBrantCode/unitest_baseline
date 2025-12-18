"""
QUESTION:
Write a function `maxSubArray` that takes in an array of integers `nums` and returns the sum of the largest contiguous subarray. The function should contain at least one number and should return the maximum sum found in the array. The input array `nums` can contain both positive and negative integers.
"""

from typing import List

def maxSubArray(nums: List[int]) -> int:
    current_max = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(current_max, global_max)
    return global_max