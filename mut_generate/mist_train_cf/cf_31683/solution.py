"""
QUESTION:
Write a function `two_sum` that takes a list of integers `nums` and a target integer `target` as input, and returns a list of two indices corresponding to the two numbers in `nums` that add up to `target`. Assume that each input has exactly one solution, and no element can be used twice. The function should be efficient and return the indices of the two numbers in the order they appear in `nums`.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    num_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num] = i
    return []