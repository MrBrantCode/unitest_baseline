"""
QUESTION:
Create a function called `create_lower_triangular_matrix` that initializes a 10x10 two-dimensional array with integer elements, sets each element below and on the main diagonal to a specified numeric value, and sets all elements above the main diagonal to zero. The function should then return the created matrix.
"""

import numpy as np

def create_lower_triangular_matrix(size, value):
    """
    Creates a size x size lower triangular matrix filled with a specified numeric value.

    Args:
        size (int): The size of the matrix.
        value (int): The value to fill the lower triangular elements with.

    Returns:
        numpy.ndarray: A size x size lower triangular matrix filled with the specified value.
    """
    matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(i+1):
            matrix[i][j] = value
    return matrix