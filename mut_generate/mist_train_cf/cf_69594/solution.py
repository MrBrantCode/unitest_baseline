"""
QUESTION:
Compute the eigenvalues and eigenvectors of a given square matrix. Write a function `compute_eigen` that takes a square matrix as input and returns a tuple of two arrays: one for the eigenvalues and one for the eigenvectors. The matrix must have the same number of rows and columns, and the function should work for both real-valued and complex-valued matrices. Use the NumPy library to efficiently compute the eigenvalues and eigenvectors.
"""

import numpy as np

def compute_eigen(matrix):
    """
    Compute the eigenvalues and eigenvectors of a given square matrix.

    Args:
        matrix (numpy.ndarray): A square matrix.

    Returns:
        tuple: A tuple of two arrays, one for the eigenvalues and one for the eigenvectors.
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors