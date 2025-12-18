"""
QUESTION:
Implement a function `reshape_array(arr, num_rows)` where `arr` is a 1D array of integers and `num_rows` is an integer representing the number of rows in the reshaped 2D array. The function should return the reshaped 2D array if the length of `arr` is divisible by `num_rows`, otherwise return "Reshaping not possible".
"""

import numpy as np

def reshape_array(arr, num_rows):
    if len(arr) % num_rows == 0:
        return np.array(arr).reshape(num_rows, -1)
    else:
        return "Reshaping not possible"