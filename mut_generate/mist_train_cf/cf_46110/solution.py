"""
QUESTION:
Write a function to find the index of the smallest value in a 2D numpy array. The function should return a tuple containing the row and column index of the smallest value. The solution should work for any arbitrary 2D numpy array.
"""

import numpy as np

def find_smallest_value_index(array):
    """
    This function finds the index of the smallest value in a 2D numpy array.

    Args:
        array (numpy.ndarray): A 2D numpy array.

    Returns:
        tuple: A tuple containing the row and column index of the smallest value.
    """
    return np.unravel_index(array.argmin(), array.shape)