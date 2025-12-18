"""
QUESTION:
Implement a function `find_furthest_elements_with_indices` that takes a list of at least two numerical values and returns a tuple containing the two non-consecutive elements with the greatest difference between them, along with their indices. The output should contain the lower value first, then its index, followed by the higher value and its index.
"""

from typing import List, Tuple

def find_furthest_elements_with_indices(numbers: List[float]) -> Tuple[float, int, float, int]:
    min_element = numbers[0]
    min_index = 0
    max_element = numbers[1]
    max_index = 1
    for i, number in enumerate(numbers):
        if number < min_element:
            min_element = number
            min_index = i
        elif number > max_element and i != min_index + 1:
            max_element = number
            max_index = i
    
    return (min_element, min_index, max_element, max_index)