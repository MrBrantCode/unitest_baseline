"""
QUESTION:
Write a function named `flatten_3d_array` that takes a 3D numpy array as input and returns a 2D numpy array. The function should combine the first two dimensions of the 3D array and keep the third dimension as columns in the output 2D array. The function should not use explicit loops to deconstruct the 3D structure.
"""

import numpy as np

def flatten_3d_array(arr):
    return arr.reshape(-1, arr.shape[-1])