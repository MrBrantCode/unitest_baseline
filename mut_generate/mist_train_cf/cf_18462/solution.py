"""
QUESTION:
Write a function named `multiply_matrices` that takes two 3x3 matrices as input and returns their product, also a 3x3 matrix, using the NumPy package.
"""

import numpy as np

def multiply_matrices(matrix1, matrix2):
    """
    This function takes two 3x3 matrices as input and returns their product.
    
    Parameters:
    matrix1 (numpy array): The first 3x3 matrix.
    matrix2 (numpy array): The second 3x3 matrix.
    
    Returns:
    numpy array: The product of the two input matrices.
    """
    return np.dot(matrix1, matrix2)