"""
QUESTION:
Create a function `calculate_std_dev` that calculates the standard deviation of a set of numbers using the NumPy library. The function should take a list of numbers as input and return the standard deviation of the input list.
"""

import numpy as np

def calculate_std_dev(numbers):
    """
    Calculate the standard deviation of a set of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The standard deviation of the input list.
    """
    return np.std(numbers)