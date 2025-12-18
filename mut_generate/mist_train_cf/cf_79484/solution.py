"""
QUESTION:
Construct a function `rolling_max_min_indices` that takes a list of integers as input and returns a list of tuples. Each tuple should contain two pairs of values: the maximum value and its index up to that point in the sequence, and the minimum value and its index up to that point in the sequence. The function should iterate through the input list and update the maximum and minimum values and their indices accordingly. The input list is a list of integers and may be empty. The output is a list of tuples of pairs, where each pair is a tuple of an integer and its index.
"""

from typing import List, Tuple

def rolling_max_min_indices(numbers: List[int]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    if not numbers:
        return []

    current_max = current_min = numbers[0]
    max_index = min_index = 0
    result = []

    for i, num in enumerate(numbers):
        if num > current_max:
            current_max = num
            max_index = i
        if num < current_min:
            current_min = num
            min_index = i
        result.append(((current_max, max_index), (current_min, min_index)))

    return result