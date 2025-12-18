"""
QUESTION:
Implement a function `find_pair_indices` that finds the indices of the pair of numbers in a given list `nums` that add up to a given `target`. The function should return a tuple of two indices. If no such pair exists, it should return None. You can use the `run_test` function from the `tests` module to find a number in a list.
"""

from typing import List, Optional, Tuple

def find_pair_indices(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    for i in range(len(nums)):
        complement = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == complement:
                return (i, j)
    return None