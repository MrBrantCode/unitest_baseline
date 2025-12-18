"""
QUESTION:
Write a function called `analyze_matrix` that calculates the eigenvalues and eigenvectors of a given matrix M and returns the results. The matrix M should be a 3x3 matrix with integer entries. The function should be able to handle repeated eigenvalues and return a basis for the corresponding eigenspace.
"""

import numpy as np

def analyze_matrix(matrix):
    """
    This function calculates the eigenvalues and eigenvectors of a given 3x3 matrix M.
    
    Parameters:
    matrix (numpy array): A 3x3 matrix with integer entries.
    
    Returns:
    eigenvalues (list): A list of eigenvalues of the matrix.
    eigenvectors (numpy array): A 2D array where each column is an eigenvector.
    """
    
    # Compute the eigenvalues and eigenvectors of the matrix
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Find the indices of the repeated eigenvalues
    repeated_eigenvalue_idx = np.where(np.diff(np.sort(eigenvalues)) == 0)[0]
    
    # If there are repeated eigenvalues, compute the corresponding eigenvectors
    if len(repeated_eigenvalue_idx) > 0:
        repeated_eigenvalue = eigenvalues[repeated_eigenvalue_idx[0]]
        null_space = np.array([eigenvectors[:, repeated_eigenvalue_idx[0]], eigenvectors[:, repeated_eigenvalue_idx[0]+1]])
        return eigenvalues, null_space
    
    else:
        return eigenvalues, eigenvectors

# No test case is provided in this code snippet.