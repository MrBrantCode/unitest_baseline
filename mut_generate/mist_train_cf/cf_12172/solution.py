"""
QUESTION:
Write a function `reshape_array` that takes a 3-dimensional numpy array `arr` of shape (n, m, k) and returns a 2-dimensional numpy array of shape (n*m, k).
"""

import numpy as np

def reshape_array(arr):
    """
    Reshapes a 3-dimensional numpy array of shape (n, m, k) to a 2-dimensional numpy array of shape (n*m, k).
    
    Parameters:
    arr (numpy array): The 3-dimensional numpy array to be reshaped.
    
    Returns:
    numpy array: A 2-dimensional numpy array of shape (n*m, k).
    """
    n, m, k = arr.shape
    return arr.reshape(n * m, k)