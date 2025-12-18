"""
QUESTION:
Create a function called `matrix_rank` that determines the rank of a given square matrix. The matrix is a 2D list of integers and its rank is the maximum number of linearly independent rows or columns. The function should return the rank of the matrix.
"""

import numpy as np

def matrix_rank(matrix):
    """
    This function calculates the rank of a given square matrix.
    
    Parameters:
    matrix (list): A 2D list of integers representing the matrix.
    
    Returns:
    int: The rank of the matrix.
    """
    # Convert the given matrix to a numpy array for easier manipulation
    matrix = np.array(matrix)
    
    # Use numpy's matrix_rank function to calculate the rank
    rank = np.linalg.matrix_rank(matrix)
    
    return rank