"""
QUESTION:
Create a function `select_elements` that takes two parameters: a 3D NumPy array `a` with dimensions N x M x 2 and a 2D NumPy array `b` with dimensions N x M containing 0s and 1s. The function should return a 2D NumPy array with dimensions N x M, where each element at position (i, j) is selected from the third dimension of `a` at position (i, j) based on the corresponding index in `b`. If the value in `b` is 0, select the first element in the third dimension of `a`, and if the value in `b` is 1, select the second element.
"""

import numpy as np

def select_elements(a, b):
    """
    Select elements from a 3D NumPy array based on indices in a 2D NumPy array.

    Parameters:
    a (numpy.ndarray): 3D NumPy array with dimensions N x M x 2.
    b (numpy.ndarray): 2D NumPy array with dimensions N x M containing 0s and 1s.

    Returns:
    numpy.ndarray: 2D NumPy array with dimensions N x M.
    """
    return np.take_along_axis(a, np.expand_dims(b, axis=-1), axis=-1).squeeze(-1)