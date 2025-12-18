"""
QUESTION:
Write a function named `analyze_eigen` that takes a 3x3 matrix M as input and returns the eigenvalues and eigenvectors of M. The function should be able to handle the case where the matrix is singular (i.e., has an eigenvalue of zero) and return the corresponding eigenvector(s).
"""

import numpy as np

def analyze_eigen(M):
    """
    Compute eigenvalues and eigenvectors of a 3x3 matrix M.
    
    Parameters:
    M (list): A 3x3 matrix.
    
    Returns:
    eigenvalues (list): Eigenvalues of the matrix M.
    eigenvectors (list): Eigenvectors of the matrix M.
    """
    # Convert the input matrix to a numpy array
    M = np.array(M)
    
    # Compute eigenvalues and eigenvectors using numpy's linalg.eig function
    eigenvalues, eigenvectors = np.linalg.eig(M)
    
    return eigenvalues, eigenvectors