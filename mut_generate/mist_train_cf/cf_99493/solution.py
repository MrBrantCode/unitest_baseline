"""
QUESTION:
Create a function `check_matrix_inversion` that takes a 2x2 matrix as input. The function should invert the matrix using `numpy.linalg.inv` and then check if the inverted matrix is not equal to the original matrix using the `not` operator and `numpy.array_equal`. The function should return a boolean indicating whether the inverted matrix is not equal to the original matrix.
"""

import numpy as np

def check_matrix_inversion(matrix):
    """
    This function checks if the inverted matrix is not equal to the original matrix.

    Parameters:
    matrix (numpy array): A 2x2 matrix.

    Returns:
    bool: True if the inverted matrix is not equal to the original matrix, False otherwise.
    """
    inv_matrix = np.linalg.inv(matrix)
    return not np.array_equal(inv_matrix, matrix)