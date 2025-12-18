"""
QUESTION:
Create a function named `check_matrix_inversion` that uses the `numpy.linalg.inv` function to invert a given 2x2 matrix and checks if the result is not equal to the original matrix. The function should take a 2x2 matrix as input, invert it, and return a boolean value indicating whether the inverted matrix is not equal to the original matrix.
"""

import numpy as np

def check_matrix_inversion(matrix):
    """
    This function checks if the inverted matrix is not equal to the original matrix.

    Args:
        matrix (numpy.ndarray): A 2x2 matrix.

    Returns:
        bool: True if the inverted matrix is not equal to the original matrix, False otherwise.
    """
    inv_matrix = np.linalg.inv(matrix)
    return not np.array_equal(inv_matrix, matrix)