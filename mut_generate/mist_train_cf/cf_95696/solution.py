"""
QUESTION:
Reduce a 3-dimensional numpy array of shape (n, m, k) to a 2-dimensional numpy array of shape (n*m, k), where all elements from the original array are included. Implement a function `reduce_3d_array(arr)` that achieves this transformation with a time complexity of O(n*m*k) and a space complexity of O(n*m*k).
"""

import numpy as np

def reduce_3d_array(arr):
    # Get the shape of the original array
    n, m, k = arr.shape
    
    # Reshape the array to a 2D array of shape (n*m, k)
    return arr.reshape((n*m, k))