"""
QUESTION:
Write a function `check_skew_symmetric(matrix)` that checks if a given square matrix is skew-symmetric and has a size of at least 2x2. The function should return `True` if the matrix is skew-symmetric, meaning it is equal to the negation of its transpose and all its diagonal elements are zero, and `False` otherwise.
"""

import numpy as np

def check_skew_symmetric(matrix):
    matrix = np.array(matrix)
    
    if matrix.shape[0] < 2 or matrix.shape[1] < 2:
        return False
    
    transpose = matrix.transpose()
    
    if np.array_equal(matrix, -transpose) and np.all(np.diag(matrix) == 0):
        return True
    
    return False