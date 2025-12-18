"""
QUESTION:
Create a function named `invert_matrix` that receives a 5x5 bi-dimensional matrix as input. The function should return the inverse of the input matrix. The input must be a square matrix (number of rows equals the number of columns) and invertible (non-zero determinant). If the input matrix does not meet these conditions, the function should return an informative error message.
"""

import numpy as np

def invert_matrix(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return 'Error: The input matrix is not square'
  
    # Check if the matrix is invertible
    det = np.linalg.det(matrix)
    if det == 0:
        return 'Error: The input matrix is not invertible'

    return np.linalg.inv(matrix)