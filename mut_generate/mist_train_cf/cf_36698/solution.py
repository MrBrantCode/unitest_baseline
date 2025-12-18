"""
QUESTION:
Given an array of integers `nums` of length `n`, write a function `minUnsortedSubarray` that takes in the array `nums` and returns the minimum length of a contiguous subarray, such that sorting this subarray would make the whole array sorted in non-decreasing order. If the array is already sorted, return 0.
"""

from typing import List

def minUnsortedSubarray(nums: List[int]) -> int:
    n = len(nums)
    sorted_nums = sorted(nums)
    start = n
    end = 0
    
    for i in range(n):
        if nums[i] != sorted_nums[i]:
            start = min(start, i)
            end = max(end, i)
    diff = end - start
    
    return diff + 1 if diff > 0 else 0