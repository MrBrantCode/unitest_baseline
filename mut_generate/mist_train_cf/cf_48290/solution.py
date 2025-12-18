"""
QUESTION:
Write a function called `matrix_rank` that calculates the rank of a given 3x3 matrix. The function should take a 3x3 matrix as input and return the rank of the matrix. The matrix is guaranteed to contain only the digit 1 in all its components.
"""

import numpy as np

def matrix_rank(matrix):
    """
    Calculate the rank of a given 3x3 matrix.
    
    Args:
    matrix (list of lists): A 3x3 matrix containing only the digit 1 in all its components.
    
    Returns:
    int: The rank of the matrix.
    """
    
    # Convert the input matrix into a numpy array
    matrix = np.array(matrix)
    
    # Perform row operations to transform the matrix into Row-Echelon Form
    # Subtract the first row from the second and third rows
    matrix[1] -= matrix[0]
    matrix[2] -= matrix[0]
    
    # Count the number of non-zero rows to determine the rank
    rank = np.count_nonzero(np.any(matrix, axis=1))
    
    return rank