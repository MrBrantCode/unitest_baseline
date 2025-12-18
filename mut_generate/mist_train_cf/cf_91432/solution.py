"""
QUESTION:
Write a function named `multiply_large_list` that takes a list of numbers as input and returns the product of all numbers in the list. The input list should have at least 10,000 elements. The function should be able to handle large lists efficiently.
"""

import numpy as np

def multiply_large_list(numbers):
    """
    Calculate the product of all numbers in a large list.
    
    Parameters:
    numbers (list): A list of numbers with a length of at least 10,000.
    
    Returns:
    float: The product of all numbers in the list.
    """
    return np.prod(numbers)