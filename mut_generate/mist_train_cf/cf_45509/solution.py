"""
QUESTION:
Create a function `calculate_determinants(matrix)` that calculates the determinant of each 5x5 sub-matrix from a given 5x10 matrix. The function should take a 5x10 2D numpy array as input, extract all possible 5x5 sub-matrices from the input matrix, and return a list of their determinants.
"""

import numpy as np

def calculate_determinants(matrix):
    # Number of 5x5 submatrices in a 5x10 matrix 
    num_submatrices = matrix.shape[1] - 4 

    determinants = []
    # Go through each 5x5 submatrix
    for i in range(num_submatrices):
        submatrix = matrix[:, i:i+5] 
        det = np.linalg.det(submatrix) # Calculate determinant
        determinants.append(det)
    return determinants