"""
QUESTION:
Find the eigenvalues and eigenvectors of a given matrix B = [[5, 7, -11], [-10, -14, 22], [20, 28, -44]]. The function should take this matrix as input and return its eigenvalues and corresponding eigenvectors.
"""

import numpy as np

def entrance(matrix):
    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    return eigenvalues, eigenvectors

# Example usage:
B = np.array([[5, 7, -11], [-10, -14, 22], [20, 28, -44]])
eigenvalues, eigenvectors = entrance(B)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)