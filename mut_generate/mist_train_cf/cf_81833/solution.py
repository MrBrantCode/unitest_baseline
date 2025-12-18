"""
QUESTION:
Given a square matrix A, write a function `null_space_dimension` to calculate the dimensionality of its null space. The null space of a matrix is the set of all vectors that the matrix maps to the zero vector. The function should take the matrix A as input and return the dimension of its null space. The dimension of the null space is given by the number of columns of the matrix minus its rank (number of linearly independent rows or columns).
"""

import numpy as np

def null_space_dimension(matrix):
    """
    Calculate the dimensionality of the null space of a square matrix.

    Args:
    matrix (numpy array): A square matrix.

    Returns:
    int: The dimension of the null space.
    """
    # Ensure the input is a numpy array
    matrix = np.array(matrix)

    # Check if the matrix is square
    assert matrix.shape[0] == matrix.shape[1], "The input matrix must be square."

    # Calculate the rank of the matrix
    rank = np.linalg.matrix_rank(matrix)

    # The dimension of the null space is the number of columns minus the rank
    null_space_dim = matrix.shape[1] - rank

    return null_space_dim