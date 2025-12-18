"""
QUESTION:
Write a function `twoSum` that finds the indices of two numbers in a list `nums` that add up to a given `target`. Assume there is exactly one solution, and elements cannot be used twice. The function should return a tuple of two indices.
"""

from typing import List, Tuple

def twoSum(nums: List[int], target: int) -> Tuple[int, int]:
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return num_indices[complement], i
        num_indices[num] = i
    return -1, -1  # If no solution is found