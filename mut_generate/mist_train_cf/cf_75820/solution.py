"""
QUESTION:
Write a function `null_space_dimension` to calculate the dimension of the null space of a given matrix. The function should take a 2D list of integers or floats representing the matrix as input, and return the dimension of its null space. Assume the input matrix is a square matrix (i.e., it has the same number of rows and columns) and does not contain any non-numeric values.
"""

import numpy as np

def null_space_dimension(matrix):
    # Convert the input matrix to a numpy array
    matrix = np.array(matrix)
    
    # Calculate the rank of the matrix
    rank = np.linalg.matrix_rank(matrix)
    
    # The dimension of the null space is n - rank(A)
    null_space_dim = len(matrix) - rank
    
    return null_space_dim