"""
QUESTION:
Create a function named `sum_odd_elements` that takes a 2D numpy array as input. The array must have at least 2 rows and 3 columns. The function should return the sum of all elements in the array that are not divisible by 2.
"""

import numpy as np

def sum_odd_elements(arr):
    """
    This function calculates the sum of all odd elements in a given 2D numpy array.

    Parameters:
    arr (numpy array): A 2D numpy array with at least 2 rows and 3 columns.

    Returns:
    int: The sum of all odd elements in the array.
    """

    # Create a boolean mask for elements that are divisible by 2
    mask = arr % 2 != 0

    # Apply the mask to the array and compute the sum
    sum_of_elements = np.sum(arr[mask])
    
    return sum_of_elements