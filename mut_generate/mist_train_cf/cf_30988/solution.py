"""
QUESTION:
Write a function `upgrade()` that takes an array of integers as input and returns a new array where each element is the sum of itself and all previous elements in the input array. The function should be efficient for large input arrays.

Function signature: `def upgrade(arr: List[int]) -> List[int]`
"""

from typing import List

def upgrade(arr: List[int]) -> List[int]:
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result