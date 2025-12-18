"""
QUESTION:
Write a function called `pseudo_inverse` that calculates the pseudo inverse of a square symmetric covariance matrix using eigenvalue decomposition and regularization. The function should take two parameters: `matrix`, the covariance matrix, and `threshold`, the minimum eigenvalue for regularization. The function should return the pseudo inverse of the matrix.
"""

import numpy as np

def pseudo_inverse(matrix, threshold):
    """
    Calculate the pseudo inverse of a square symmetric covariance matrix using eigenvalue decomposition and regularization.

    Parameters:
    matrix (numpy array): The covariance matrix.
    threshold (float): The minimum eigenvalue for regularization.

    Returns:
    numpy array: The pseudo inverse of the matrix.
    """
    
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    
    # Apply regularization
    eigenvalues = np.maximum(eigenvalues, threshold)
    
    # Calculate the inverse of the eigenvalues
    inverse_eigenvalues = 1 / eigenvalues
    
    # Construct the pseudo inverse matrix
    pseudo_inverse_matrix = eigenvectors @ np.diag(inverse_eigenvalues) @ eigenvectors.T
    
    return pseudo_inverse_matrix