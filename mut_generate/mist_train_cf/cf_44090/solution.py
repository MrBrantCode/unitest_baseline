"""
QUESTION:
Create a function `rolling_max(numbers1, numbers2)` that takes two lists of integers `numbers1` and `numbers2` as input. The function should return a list of integers representing the rolling maximum element found until the given moment in the sequence, comparing the elements from both input lists in sequence up to that point. The function should assume that both input lists are of the same length.
"""

from typing import List

def rolling_max(numbers1: List[int], numbers2: List[int]) -> List[int]:
    result = []
    max_so_far1 = max_so_far2 = float('-inf')
    for num1, num2 in zip(numbers1, numbers2):
        max_so_far1 = max(max_so_far1, num1)
        max_so_far2 = max(max_so_far2, num2)
        result.append(max(max_so_far1, max_so_far2))
    return result