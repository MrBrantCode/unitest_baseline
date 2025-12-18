"""
QUESTION:
Given an integer array `nums`, find the shortest continuous subarray that, when sorted in ascending order, makes the whole array sorted in ascending order. If multiple subarrays satisfy this condition, return the one starting at the lowest index. If no such subarray exists, return -1. The function should be `findUnsortedSubarray(nums)`. The constraints are `1 <= nums.length <= 104` and `-105 <= nums[i] <= 105`, and `nums[i] != nums[i+1]` for all `0 <= i < nums.length - 1`.
"""

def findUnsortedSubarray(nums):
    sorted_nums = sorted(nums)
    start = end = -1

    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            if start == -1:
                start = i
            end = i

    if start == -1: 
        return 0
    else: 
        return end - start + 1