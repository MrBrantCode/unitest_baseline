"""
QUESTION:
Write a function `calculate_inverse(matrix)` that takes a square matrix as input, calculates its inverse, and returns a dictionary containing the inverse matrix and its determinant. If the input matrix is not invertible, the function should return an error message. The input matrix must be a square matrix (i.e., have the same number of rows and columns).
"""

import numpy as np

def calculate_inverse(matrix):
    try:
        inverse_matrix = np.linalg.inv(matrix)
        det = np.linalg.det(matrix)
        return { 'inverse': inverse_matrix, 'determinant': det}

    except np.linalg.LinAlgError:
        return "The matrix is not invertible."