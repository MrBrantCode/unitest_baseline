"""
QUESTION:
Create a function called `calculate_determinants` that takes a 2x4 matrix as input. The function should first calculate the transpose of the input matrix. Then, it should calculate the determinants of all possible 2x2 sub-matrices that can be formed from the transposed matrix, where each sub-matrix starts from the first row to the second last row of the transposed matrix. The function should return the determinants of these sub-matrices in a list.
"""

import numpy as np

def calculate_determinants(matrix):
    """
    Calculate the determinants of all possible 2x2 sub-matrices 
    that can be formed from the transposed input matrix.

    Args:
    matrix (numpy array): A 2x4 matrix.

    Returns:
    list: A list of determinants of the 2x2 sub-matrices.
    """

    # Calculate the transpose of the input matrix
    matrix_t = matrix.T

    # Initialize an empty list to store the determinants
    determinants = []

    # Loop through the transpose matrix and consider every 2x2 matrix
    for i in range(len(matrix_t) - 1):
        sub_matrix = matrix_t[i:i+2]
        det = np.linalg.det(sub_matrix)
        determinants.append(det)

    return determinants