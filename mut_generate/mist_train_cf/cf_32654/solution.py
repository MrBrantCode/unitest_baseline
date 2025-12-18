"""
QUESTION:
Transform a given numpy array to have a specific number of rows by repeating its last row if necessary. 

Create a function `transform_array` that takes in a numpy array `nump_array` and an integer `expected_shape` representing the desired number of rows. The function should return the transformed array with the expected number of rows. If the array's current number of rows is less than the expected shape, repeat the last row of the array to make up the difference.
"""

import numpy as np

def transform_array(nump_array, expected_shape):
    if nump_array.shape[0] != expected_shape:
        diff = expected_shape - nump_array.shape[0]
        if diff > 0:
            last_row = nump_array[-1]  # Get the last row of the array
            repeat_rows = np.tile(last_row, (diff, 1))  # Repeat the last row to match the expected shape
            nump_array = np.concatenate((nump_array, repeat_rows), axis=0)  # Concatenate the repeated rows to the original array
    return nump_array