"""
QUESTION:
Implement a function `find_target_indices(nums, target)` that takes a list of integers `nums` and a target value `target` as input, and returns a list of tuples, where each tuple contains the indices of two elements from the input list that sum up to the target value. If no such pair exists, return an empty list.
"""

from typing import List, Tuple

def find_target_indices(nums: List[int], target: int) -> List[Tuple[int, int]]:
    num_indices = {}
    result = []
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            result.append((num_indices[complement], i))
        num_indices[num] = i
    
    return result