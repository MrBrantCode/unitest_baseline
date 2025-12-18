"""
QUESTION:
Create a function named `create_matrix` that takes a 1D array as input and returns a 2D matrix. The input array should be padded with zeros to a minimum length of 4 if necessary. The matrix should have a number of rows equal to the length of the padded array, and each row should be the input array multiplied by a different power of 2, starting from 2^0.
"""

import numpy as np

def create_matrix(arr):
    # insert zeros to match the length with the max size
    max_len = max(4, len(arr))
    arr = np.pad(arr, (0, max_len - len(arr)), 'constant', constant_values=(0))

    # create matrix by multiplying each row with different power of 2
    mat = np.array([arr * (2 ** i) for i in range(max_len)])
    
    return mat