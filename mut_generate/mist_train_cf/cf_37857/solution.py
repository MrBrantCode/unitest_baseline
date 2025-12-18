"""
QUESTION:
Write a function `findUnsortedSubarray(nums)` that finds the shortest subarray that, when sorted, makes the entire array sorted in non-decreasing order. The function takes a list of unique integers `nums` as input, where 1 <= len(nums) <= 10^4 and all elements are within the range [-10^5, 10^5]. Return the length of the subarray. If the array is already sorted, return 0.
"""

from typing import List

def findUnsortedSubarray(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    start, end = len(nums), 0
    
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            start = min(start, i)
            end = max(end, i)
    
    return end - start + 1 if end - start >= 0 else 0