"""
QUESTION:
Implement a function `nparray_and_transpose(data_a_b_c)` that takes a 3D nested list `data_a_b_c` of shape (a, b, c) as input, converts it into a NumPy array, and returns the transposed array of shape (a, c, b).
"""

import numpy as np

def nparray_and_transpose(data_a_b_c):
    # Convert the nested list to a NumPy array
    arr = np.array(data_a_b_c)
    
    # Transpose the array
    transposed_arr = np.transpose(arr, axes=(0, 2, 1))
    
    return transposed_arr