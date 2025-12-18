"""
QUESTION:
Write a function `multiply_numbers` that takes a list of numbers as input and returns their product, with the constraint that the function should be able to handle lists of at least 10,000 numbers.
"""

import numpy as np

def multiply_numbers(numbers):
    """
    This function calculates the product of all numbers in the input list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    float: The product of all numbers in the list.
    """
    return np.prod(numbers)