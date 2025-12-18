"""
QUESTION:
Write a function `find_numbers(factors, target)` that takes a list of integers `factors` and an integer `target` as input and returns a tuple of two integers. The function should find two distinct integers in the list of factors that add up to the target value. If there are multiple valid solutions, any one can be returned. The solution should have a time complexity of O(n), where n is the number of factors provided.
"""

from typing import List, Tuple

def entrance(factors: List[int], target: int) -> Tuple[int, int]:
    seen = set()
    for factor in factors:
        complement = target - factor
        if complement in seen:
            return (complement, factor)
        seen.add(factor)
    return None  # Return None if no solution is found