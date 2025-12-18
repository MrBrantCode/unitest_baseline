"""
QUESTION:
Implement the function `find_pair_sum(nums: List[int], target: int) -> List[int]` where `nums` is a list of integers with a length between 1 and 10^5 (inclusive) and `target` is the target sum with a value between 1 and 10^9 (inclusive). The function should return a pair of integers from the list that add up to the target sum, prioritizing the pair with the lowest indices if duplicates exist. If no such pair exists, return an empty list.
"""

from typing import List

def find_pair_sum(nums: List[int], target: int) -> List[int]:
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [complement, num] if num_indices[complement] < i else [num, complement]
        num_indices[num] = i
    return []