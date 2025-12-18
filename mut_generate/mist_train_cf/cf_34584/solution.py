"""
QUESTION:
Generate a sequence of a specified number of elements where the first two elements are 0 and 1, and each subsequent element is the sum of the two preceding elements.

The function should be named `generate_sequence` and take an integer `num_elements` as input, returning a list of integers.
"""

from typing import List

def generate_sequence(num_elements: int) -> List[int]:
    if num_elements <= 0:
        return []
    elif num_elements == 1:
        return [0]
    elif num_elements == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, num_elements):
            next_element = sequence[i-1] + sequence[i-2]
            sequence.append(next_element)
        return sequence