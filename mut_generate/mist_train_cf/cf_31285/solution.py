"""
QUESTION:
Implement the function `transform_array(arr)` that takes a 2D NumPy array `arr` as input, reshapes it into a 1D array, and applies the transformation to each element: if the element is less than 0.5, replace it with its square; otherwise, replace it with twice the element minus 1. The function should return the resulting array. The input array should be reshaped into a 1D array using the `reshape(-1)` method. The transformation should be applied using the `np.where` function from the NumPy library.
"""

import numpy as np

def transform_array(arr):
    return np.where(arr.reshape(-1) < 0.5, arr.reshape(-1)**2, 2*arr.reshape(-1) - 1)