"""
QUESTION:
Write a function `min_position(b)` that finds the position (indices) of the smallest value in a multi-dimensional NumPy array `b` and returns the unraveled index in Fortran order.
"""

import numpy as np

def min_position(b):
    return np.unravel_index(np.argmin(b, axis=None), b.shape, order='F')