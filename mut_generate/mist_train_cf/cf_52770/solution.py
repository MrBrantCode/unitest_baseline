"""
QUESTION:
Write a function named `rotate_ndarray` that takes in a numpy array and an integer `n`, representing the number of dimensions in the array. The function should return the input array rotated 90 degrees counter-clockwise on each level. The function should be able to handle any dimension of numpy array inputted. Note that rotation is not applicable to arrays of less than two dimensions, so the function should return the original array in this case.
"""

import numpy as np

def rotate_ndarray(arr, n):
    if n < 2:
        print("Rotation is not applicable to arrays of less than two dimensions")
        return arr
    
    return np.rot90(arr, axes=(n-2,n-1))