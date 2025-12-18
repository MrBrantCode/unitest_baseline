"""
QUESTION:
Compute the determinant and rank of a given 3x3 matrix. 

The function, `dissect_matrix`, should take as input a 3x3 matrix `C` and return its determinant and rank. The function should also check if the determinant is zero before calculating it and if the rows are linearly dependent to determine the rank.
"""

import numpy as np

def dissect_matrix(C):
    """
    Compute the determinant and rank of a given 3x3 matrix.
    
    Args:
        C (list): A 3x3 matrix.
    
    Returns:
        tuple: A tuple containing the determinant and rank of the matrix.
    """
    
    # Convert the input list into a numpy array
    C = np.array(C)
    
    # Check if the determinant is likely to be zero
    if np.any(np.all(C == 0, axis=1)) or np.any(np.all(C[:, 1:] == C[:, :-1], axis=0)):
        det = 0
    else:
        # Compute the determinant using numpy's built-in function
        det = np.linalg.det(C)
        
        # If the determinant is close to zero, set it to zero
        if abs(det) < 1e-6:
            det = 0
    
    # Compute the rank of the matrix
    rank = np.linalg.matrix_rank(C)
    
    return det, rank