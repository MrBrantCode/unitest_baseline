"""
QUESTION:
Write a function called `check_matrix_inversion` that takes a 2x2 matrix as input, inverts it using `numpy.linalg.inv`, and checks if the inverted matrix is not equal to the original matrix using the logical operator "not" and `numpy.array_equal`.
"""

import numpy as np

def check_matrix_inversion(matrix):
    """
    Inverts a 2x2 matrix using numpy.linalg.inv and checks if the inverted matrix is not equal to the original matrix.

    Args:
        matrix (numpy.ndarray): A 2x2 matrix.

    Returns:
        bool: True if the inverted matrix is not equal to the original matrix, False otherwise.
    """
    inv_matrix = np.linalg.inv(matrix)
    return not np.array_equal(inv_matrix, matrix)