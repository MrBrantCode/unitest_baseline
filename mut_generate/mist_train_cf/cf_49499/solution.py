"""
QUESTION:
Create a function `nullity_of_matrix` that calculates the dimension of the null space of a given matrix. The function should take a 2D list representing the matrix as input and return the nullity of the matrix. The matrix is a list of lists where each inner list represents a row in the matrix. The nullity is the dimension of the null space of the matrix.
"""

import numpy as np

def nullity_of_matrix(matrix):
    """
    Calculate the dimension of the null space of a given matrix.
    
    Args:
        matrix (list): A 2D list representing the matrix.
        
    Returns:
        int: The nullity of the matrix.
    """
    # Convert the given matrix to a numpy array
    A = np.array(matrix)
    
    # Calculate the rank of the matrix
    rank = np.linalg.matrix_rank(A)
    
    # Calculate the nullity of the matrix using the Rank-Nullity Theorem
    nullity = A.shape[1] - rank
    
    return nullity