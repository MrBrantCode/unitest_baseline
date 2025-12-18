"""
QUESTION:
Create a function named `matrix_rank` that determines the rank of a given matrix. The matrix is a 2D list of integers with identical rows and columns. The function should calculate and return the rank of the matrix.
"""

import numpy as np

def matrix_rank(matrix):
    """
    Calculate the rank of a given matrix.

    Args:
    matrix (list): A 2D list of integers with identical rows and columns.

    Returns:
    int: The rank of the matrix.
    """
    return np.linalg.matrix_rank(matrix)