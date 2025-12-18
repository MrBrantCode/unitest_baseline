"""
QUESTION:
Write a function `matrix_multiplication` that takes two 3D numpy arrays of shape `(n, 2, 2)` as input and returns their matrix multiplication result. The function should work for arrays where the last two dimensions are of size 2 but the first dimension can be any size. The last two axes of both arrays should match in size for matrix multiplication.
"""

import numpy as np

def matrix_multiplication(A, B):
    """
    This function performs matrix multiplication of two 3D numpy arrays.
    
    Parameters:
    A (numpy array): The first 3D numpy array.
    B (numpy array): The second 3D numpy array.
    
    Returns:
    result (numpy array): The matrix multiplication result of A and B.
    """
    return np.matmul(A, B)