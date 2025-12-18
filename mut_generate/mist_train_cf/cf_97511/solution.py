"""
QUESTION:
Create a function named `check_matrix_inversion` that takes a 2D list representing a matrix as input and performs the following tasks: 
- Inverts the matrix using `numpy.linalg.inv`.
- Checks if the inverted matrix is not equal to the original matrix using `not` and `numpy.array_equal`. 
The function should return a boolean value indicating whether the inverted matrix is not equal to the original matrix. The input matrix is a square matrix (i.e., it has the same number of rows and columns).
"""

import numpy as np

def check_matrix_inversion(matrix):
    """
    Checks if the inverted matrix is not equal to the original matrix.

    Args:
        matrix (2D list): A square matrix.

    Returns:
        bool: True if the inverted matrix is not equal to the original matrix, False otherwise.
    """
    inv_matrix = np.linalg.inv(np.array(matrix))
    return not np.array_equal(inv_matrix, matrix)