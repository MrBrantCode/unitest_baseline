"""
QUESTION:
Create a function called `det_eigen` that takes a complex-valued matrix `A` as input and returns its determinant and eigenvalues. Ensure the function is optimized for efficiency when handling large matrices and handle the case where the input matrix is singular (i.e., its determinant is zero).
"""

import numpy as np

def det_eigen(A):
    det = np.linalg.det(A)
    if det == 0:
        return None, None
    else:
        eigenvals = np.linalg.eigvals(A)
        return det, eigenvals