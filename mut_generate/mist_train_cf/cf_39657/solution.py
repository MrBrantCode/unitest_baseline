"""
QUESTION:
Write a function `find_pair_with_sum` that takes a list of integers `nums` and an integer `target` as input, and returns the first pair of numbers in the list that add up to `target`. If no such pair exists, the function should return `None`.
"""

from typing import List, Optional, Tuple

def find_pair_with_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    num_set = set()
    for num in nums:
        complement = target - num
        if complement in num_set:
            return (complement, num)
        num_set.add(num)
    return None