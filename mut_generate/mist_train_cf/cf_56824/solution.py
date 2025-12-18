"""
QUESTION:
Create a function named `rolling_max_min_indices` that takes a list of integers as input. The function should return a list of tuples, where each tuple contains two elements: the first element is a tuple of the maximum value and its index observed up to the current point in the sequence, and the second element is a tuple of the minimum value and its index observed up to the current point in the sequence. If the input list is empty, the function should return an empty list.
"""

from typing import List, Tuple

def rolling_max_min_indices(numbers: List[int]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    if not numbers:
    	return []
    
    max_value = min_value = numbers[0]
    max_index = min_index = 0
    output = []
    
    for index, number in enumerate(numbers):
        if number >= max_value:
            max_value = number
            max_index = index
        if number <= min_value:
            min_value = number
            min_index = index
        output.append(((max_value, max_index), (min_value, min_index)))
    return output