"""
QUESTION:
Write a function called `matrix_rank` that calculates the rank of a given square matrix. The matrix is a 3x3 matrix filled with 1s. The function should determine the maximum number of linearly independent rows or columns in the matrix and return this value as the rank of the matrix.
"""

import numpy as np

def matrix_rank(matrix):
    """
    This function calculates the rank of a given square matrix.

    Args:
        matrix (list): A 2D list representing the square matrix.

    Returns:
        int: The rank of the matrix.
    """
    # Convert the input matrix into a numpy array
    matrix = np.array(matrix)
    
    # Use numpy's linalg.matrix_rank function to calculate the rank of the matrix
    rank = np.linalg.matrix_rank(matrix)
    
    return rank