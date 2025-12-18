"""
QUESTION:
Create a function `det_eigen(A)` that calculates the determinant and eigenvalues of a complex-valued matrix `A`. The function should return a tuple containing the determinant and eigenvalues of the matrix. If the matrix is singular (i.e., its determinant is zero), the function should return `(None, None)`. The function should be optimized for efficiency and able to handle large matrices.
"""

import numpy as np

def det_eigen(A):
    det = np.linalg.det(A)
    if det == 0:
        return None, None
    else:
        eigenvals = np.linalg.eigvals(A)
        return det, eigenvals