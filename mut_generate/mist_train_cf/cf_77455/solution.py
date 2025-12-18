"""
QUESTION:
Write a function named `find_furthest_elements` that takes a list of float numbers as input and returns a tuple of two float numbers. The function should identify and return the two elements with the greatest difference between them from the given list of numbers, ensuring they are non-sequential and are returned in ascending order. The function should return `None` if the input list contains less than two elements.
"""

from typing import List, Tuple

def find_furthest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Identify and return the two elements with the greatest difference between them from a given list of numbers, ensuring they are non-sequential and are returned in ascending order.
    """
    if len(numbers) < 2:
        return None
    max_num = max(numbers)
    min_num = min(numbers)
    return (min_num, max_num)