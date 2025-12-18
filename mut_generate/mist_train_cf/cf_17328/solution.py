"""
QUESTION:
Create a function `multiply_large_list` that takes a list of at least 10,000 positive integers, each less than or equal to 100, and returns the product of all the numbers in the list.
"""

import math

def multiply_large_list(numbers):
    """
    This function takes a list of at least 10,000 positive integers, 
    each less than or equal to 100, and returns the product of all the numbers in the list.

    Args:
        numbers (list): A list of positive integers.

    Returns:
        int: The product of all numbers in the list.
    """
    return math.prod(numbers)