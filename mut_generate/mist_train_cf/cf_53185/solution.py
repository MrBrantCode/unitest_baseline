"""
QUESTION:
Write a function `flatten_3d_array` that takes a 3D numpy array as input and returns a 2D numpy array by reshaping the original array. The function should reshape the input array such that the first two dimensions are flattened into a single dimension, and the third dimension remains unchanged.
"""

import numpy as np

def flatten_3d_array(array):
    """
    This function takes a 3D numpy array as input and returns a 2D numpy array.
    The function reshapes the input array such that the first two dimensions are 
    flattened into a single dimension, and the third dimension remains unchanged.

    Parameters:
    array (numpy.ndarray): A 3D numpy array.

    Returns:
    numpy.ndarray: A 2D numpy array.
    """
    return np.reshape(array, (array.shape[0]*array.shape[1], array.shape[2]))