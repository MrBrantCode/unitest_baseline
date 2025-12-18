"""
QUESTION:
Create two functions in Python: `calculate_eigen(matrix)` and `verify_eigen(matrix, eigenvalues, eigenvectors)`. 

Function `calculate_eigen(matrix)` should take a 3x3 matrix as input and return its eigenvalues and eigenvectors. Function `verify_eigen(matrix, eigenvalues, eigenvectors)` should verify if the provided eigenvalues and eigenvectors are correct by checking if the left-hand side (`np.dot(matrix, eigenvectors[:, i])`) and right-hand side (`eigenvalues[i] * eigenvectors[:, i]`) of the eigenvalue equation are approximately equal for each eigenvalue, eigenvector pair. Use numpy for calculations.

Restrictions: The input matrices should be 3x3, and the functions should be able to handle multiple matrices. The verification function should return True if all eigenvalue, eigenvector pairs are correct and False otherwise.
"""

import numpy as np

def calculate_eigen(matrix):
    # Returns the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

def verify_eigen(matrix, eigenvalues, eigenvectors):
    # For each eigenvalue, eigenvector pair
    for i in range(len(eigenvalues)):
        # Calculating the left and right side of the eigen equation
        left = np.dot(matrix, eigenvectors[:, i])
        right = eigenvalues[i] * eigenvectors[:, i]
        # If they are not close enough, return False
        if not np.allclose(left, right):
            return False
    # If all eigenvalue, eigenvector pairs have been verified, return True
    return True