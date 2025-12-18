"""
QUESTION:
Write a function `rolling_max` that takes two lists of integers as input and returns a list of the maximum integers encountered so far at each position in the input lists. If one list is longer than the other, the remaining elements in the longer list should still be processed.
"""

from itertools import zip_longest
from typing import List

def rolling_max(numbers1: List[int], numbers2: List[int]) -> List[int]:
    max_so_far = float('-inf')
    result = []

    for n1, n2 in zip_longest(numbers1, numbers2, fillvalue=float('-inf')):
        max_so_far = max(max_so_far, n1, n2)
        result.append(max_so_far)

    return result