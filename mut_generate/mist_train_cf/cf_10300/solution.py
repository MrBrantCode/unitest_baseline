"""
QUESTION:
Write a function named `reshape_array` that takes a 1-dimensional numpy array as input and returns the reshaped array with 3 rows and 4 columns.
"""

import numpy as np

def reshape_array(arr):
    return np.reshape(arr, (3, 4))