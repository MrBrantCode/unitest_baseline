"""
QUESTION:
Write a function named `calculate_eigen` that takes a 2x2 matrix as input, calculates its eigenvalues and eigenvectors using the Numpy library, and returns them. Ensure the function can handle any 2x2 matrix input. The function should be optimized for time complexity, considering Numpy's built-in efficiency for matrix operations.
"""

import numpy as np

def calculate_eigen(matrix):
    """
    Calculate the eigenvalues and eigenvectors of a 2x2 matrix.
    
    Args:
        matrix (numpy.ndarray): A 2x2 matrix.
    
    Returns:
        eigenvalues (numpy.ndarray): The eigenvalues of the matrix.
        eigenvectors (numpy.ndarray): The eigenvectors of the matrix.
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors