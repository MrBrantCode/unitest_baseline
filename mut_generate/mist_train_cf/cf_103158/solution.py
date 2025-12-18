"""
QUESTION:
Write a function `matrix_multiply` that takes two 3x3 matrices as input and returns their product using the NumPy package. The matrices are expected to be input as 2D lists of integers. The function should return a 2D list representing the product of the input matrices.
"""

import numpy as np

def matrix_multiply(matrix1, matrix2):
    """
    This function multiplies two 3x3 matrices.

    Args:
        matrix1 (list): A 2D list representing the first matrix.
        matrix2 (list): A 2D list representing the second matrix.

    Returns:
        list: A 2D list representing the product of the input matrices.
    """
    return np.dot(matrix1, matrix2).tolist()