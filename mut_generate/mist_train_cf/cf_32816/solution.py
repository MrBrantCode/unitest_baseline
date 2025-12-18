"""
QUESTION:
Implement the `eigen_decomposition` function to take a symmetric matrix as input and return a tuple containing the eigenvalues and eigenvectors of the input matrix. Implement the `validate_eigenpairs` function to check that the input eigenvalues and eigenvectors satisfy the eigenvalue equation for the given matrix, returning `True` if the eigenvalue equation holds within a certain tolerance (1e-8) and `False` otherwise. Assume the input matrix is a NumPy array.
"""

import numpy as np
from typing import Tuple
from numpy.linalg import eigh, norm

def eigen_decomposition(matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = eigh(matrix)
    return eigenvalues, eigenvectors

def validate_eigenpairs(matrix: np.ndarray, eigenvalues: np.ndarray, eigenvectors: np.ndarray) -> bool:
    for i, value in enumerate(eigenvalues):
        residue = np.dot(matrix, eigenvectors[:, i]) - value * eigenvectors[:, i]
        if norm(residue) >= 1e-8:
            return False
    return True