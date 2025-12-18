"""
QUESTION:
Create a function `is_matrix_outlier` that determines whether a given matrix is an outlier compared to a group of known non-anomalous matrices. The function should accept two parameters: a list of known non-anomalous matrices (`known_matrices`) and a new matrix (`new_matrix`). The function should return `True` if the `new_matrix` is an outlier and `False` otherwise.
"""

import numpy as np

def is_matrix_outlier(known_matrices, new_matrix):
    """
    Determine whether a given matrix is an outlier compared to a group of known non-anomalous matrices.
    
    Parameters:
    known_matrices (list): A list of known non-anomalous matrices.
    new_matrix (numpy array): A new matrix to check for outlier status.
    
    Returns:
    bool: True if the new_matrix is an outlier, False otherwise.
    """
    
    # Compute Frobenius norm for each known matrix
    norms = [np.linalg.norm(matrix) for matrix in known_matrices]
    
    # Calculate median and median absolute deviation (MAD) of the norms
    median = np.median(norms)
    mad = np.median([abs(norm - median) for norm in norms])
    
    # Compute Frobenius norm for the new matrix
    new_norm = np.linalg.norm(new_matrix)
    
    # Check if the new matrix's norm is more than 2 MAD away from the median
    return abs(new_norm - median) > 2 * mad