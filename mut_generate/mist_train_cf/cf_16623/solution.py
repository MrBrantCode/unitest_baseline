"""
QUESTION:
Write a function `reshape_array` that takes a 2D numpy array `arr` and a target shape `shape` as input, and returns the reshaped array with the specified shape. The reshaped array should be filled with the values from the original array repeated multiple times if necessary. The function should handle cases where the target shape is not a multiple of the original shape, and return an error message in such cases.
"""

import numpy as np

def reshape_array(arr, shape):
    try:
        reshaped_arr = np.tile(arr, (shape[0] // arr.shape[0] + (1 if shape[0] % arr.shape[0] != 0 else 0), shape[1] // arr.shape[1] + (1 if shape[1] % arr.shape[1] != 0 else 0)))
        return reshaped_arr[:shape[0], :shape[1]]
    except:
        return "Error: Could not reshape array"