"""
QUESTION:
Create a function named `complex_matrix_multiply` that efficiently multiplies two given matrices, where the elements of the matrices are complex numbers. The function should return the result of the matrix multiplication. The input matrices are in the form of 2D lists of complex numbers, and the function should be able to handle matrices of any size as long as the multiplication is valid. The function should not take any other parameters besides the two matrices.
"""

import numpy as np

def complex_matrix_multiply(matrix1, matrix2):
    """
    This function efficiently multiplies two given matrices, 
    where the elements of the matrices are complex numbers.

    Args:
    matrix1 (list of lists): The first matrix.
    matrix2 (list of lists): The second matrix.

    Returns:
    numpy.ndarray: The result of the matrix multiplication.
    """
    return np.dot(np.array(matrix1), np.array(matrix2))