"""
QUESTION:
Write a function `rolling_max_min_indices` that takes a list of integers as input and returns a list of tuples, where each tuple contains the maximum and minimum elements along with their respective indices up to the current point in the sequence. The function should process the input list in a rolling manner, considering pairs of the maximum and minimum elements and their indices at each step.
"""

from typing import List, Tuple

def rolling_max_min_indices(numbers: List[int]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    res = []
    max_element = None
    min_element = None
    max_index = 0
    min_index = 0

    for i, n in enumerate(numbers):
        if max_element is None or n > max_element:
            max_element = n
            max_index = i
        if min_element is None or n < min_element:
            min_element = n
            min_index = i
        
        res.append(((max_element, max_index), (min_element, min_index)))

    return res