"""
QUESTION:
Compute the eigenvalues and eigenvectors of the given matrix M = [[5, 10, -20], [-10, -20, 40], [20, 40, -80]] and analyze the implications of the results in the context of linear algebra. The solution should take into account the matrix's properties and provide a systematic approach to calculating its eigenvalues and eigenvectors.
"""

import numpy as np

def compute_eigen(M):
    """
    Compute the eigenvalues and eigenvectors of a given matrix M.
    
    Parameters:
    M (numpy array): Input matrix.
    
    Returns:
    eigenvalues (numpy array): Eigenvalues of the input matrix.
    eigenvectors (numpy array): Eigenvectors of the input matrix.
    """
    
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(M)
    
    return eigenvalues, eigenvectors

# The rest of the code (analysis and implications) remains the same as in the original answer