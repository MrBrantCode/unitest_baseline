"""
QUESTION:
Write a function called `matrix_properties` that calculates the rank and determinant of a given 3x3 matrix. The matrix is represented as a list of three lists, each containing three integers. The function should return the rank and determinant of the matrix as a tuple. The function should assume that the input matrix is a list of three lists, each containing three integers, and that the input matrix may be singular (i.e., non-invertible).
"""

import numpy as np

def matrix_properties(matrix):
    """
    Calculate the rank and determinant of a given 3x3 matrix.

    Args:
        matrix (list of lists): A 3x3 matrix represented as a list of three lists, each containing three integers.

    Returns:
        tuple: A tuple containing the rank and determinant of the matrix.
    """

    # Convert the input matrix to a numpy array for easier calculations
    matrix = np.array(matrix)

    # Calculate the rank of the matrix
    rank = np.linalg.matrix_rank(matrix)

    # Calculate the determinant of the matrix
    determinant = np.linalg.det(matrix)

    return rank, determinant