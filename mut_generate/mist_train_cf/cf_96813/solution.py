"""
QUESTION:
Create a function named `multiply_by_index_and_add_sqrt` that takes a list of numbers as input, multiplies each number by its 1-based index position (with the first element being at index 1), adds the square root of the index position to the result, and returns a list of these calculated values. Note that the input list can contain any number of elements.
"""

import math

def multiply_by_index_and_add_sqrt(numbers):
    """
    This function takes a list of numbers, multiplies each number by its 1-based index position,
    adds the square root of the index position to the result, and returns a list of these calculated values.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of calculated values.
    """
    return [i * (idx + 1) + math.sqrt(idx + 1) for idx, i in enumerate(numbers)]