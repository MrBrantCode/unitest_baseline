"""
QUESTION:
Write a function `find_two_sum` that takes a list of integers `nums` and a target integer `target` as input, and returns a list of two distinct indices of elements in `nums` that sum up to `target`. If no such pair exists, return an empty list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the input list.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []