"""
QUESTION:
Write a function named `findMaxValue` that finds the maximum value in a multidimensional array. The function should have a time complexity of O(N), where N is the total number of elements in the array. The input array can have an arbitrary number of dimensions, and each dimension can have an arbitrary size.
"""

import numpy as np

def findMaxValue(arr):
    """
    Finds the maximum value in a multidimensional array.

    Args:
        arr (numpy.ndarray): The multidimensional array.

    Returns:
        The maximum value in the array.
    """
    return np.max(arr)