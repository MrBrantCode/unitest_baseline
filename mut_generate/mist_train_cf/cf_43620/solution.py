"""
QUESTION:
Write a function named `linear_transformation` that takes two numpy arrays as parameters, `matrix` and `transformation`, and returns the result of the linear transformation applied to the given matrix. The function should use matrix multiplication and assumes the dimensions of the input matrices are compatible for multiplication.
"""

import numpy as np

def linear_transformation(matrix, transformation):
    """
    Apply linear transformation on a given matrix.

    Parameters:
    matrix (numpy array) : Base matrix
    transformation (numpy array) : Transformation matrix

    Returns:
    numpy array: Transformed matrix
    """

    return np.dot(matrix, transformation)