"""
QUESTION:
Create a function named 'is_entangled' to determine whether a given state is entangled or not. This function should take a 2D numpy array as input, representing the density matrix of a quantum system, and return True if the state is entangled and False otherwise. The function should not use any external libraries other than NumPy.
"""

import numpy as np

def is_entangled(rho):
    """
    Determine whether a given state is entangled or not.

    Parameters:
    rho (numpy array): A 2D numpy array representing the density matrix of a quantum system.

    Returns:
    bool: True if the state is entangled, False otherwise.
    """
    # Partial transpose of the density matrix
    rho_pt = np.transpose(rho.reshape(2, 2, 2, 2), (0, 3, 1, 2)).reshape(4, 4)
    
    # Check if the partial transpose has any negative eigenvalues
    eigs = np.linalg.eigvals(rho_pt)
    return np.any(eigs < 0)