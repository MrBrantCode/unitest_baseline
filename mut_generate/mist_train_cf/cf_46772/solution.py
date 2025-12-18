"""
QUESTION:
Create a function called `calculate_standard_deviation` that takes a list of integers as input and returns the standard deviation of the list using the numpy library. The function should utilize numpy's built-in `std()` function to calculate the standard deviation.
"""

import numpy as np

def calculate_standard_deviation(numbers):
    """
    This function calculates the standard deviation of a given list of numbers.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    float: The standard deviation of the input list.
    """
    return np.std(numbers)