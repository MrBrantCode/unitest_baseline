"""
QUESTION:
Create a function named `create_matrix` that takes two parameters `n` and `m` representing the dimensions of a matrix. The function should generate a 2D matrix of size `n x m` filled with sequentially ordered even numbers starting from 0 in column-major order.
"""

import numpy as np

def create_matrix(n, m):
    # create an array of size n*m filled with even numbers starting from 0
    arr = np.arange(0, n * m * 2, 2)
    
    # reshape the array to a matrix of size n x m in column-major order (i.e., Fortran-style)
    mat = np.reshape(arr, (n, m), order='F')
    
    return mat