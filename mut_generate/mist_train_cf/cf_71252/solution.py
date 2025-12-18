"""
QUESTION:
Calculate the cumulative product of all elements in a 3D numeric array.

Write a function named `cumulative_product_3d` that takes a 3D numeric array as input and returns a 1D array with the cumulative product of each element in the original array. The function should handle arrays of any size.
"""

import numpy as np

def cumulative_product_3d(arr):
    """
    Calculate the cumulative product of all elements in a 3D numeric array.

    Parameters:
    arr (numpy array): A 3D numeric array.

    Returns:
    numpy array: A 1D array with the cumulative product of each element in the original array.
    """
    return np.cumprod(arr)