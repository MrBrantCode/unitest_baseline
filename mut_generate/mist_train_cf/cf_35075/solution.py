"""
QUESTION:
Implement a function `partial_svd` that performs partial singular value decomposition (SVD) on a given matrix. The function should take two inputs: a 2D list or numpy array `matrix` and an integer `num_singular_values` representing the maximum number of singular values to compute. It should return three outputs: the left singular vectors `U`, the singular values `S`, and the right singular vectors `V`, where `U` and `V` are 2D lists or numpy arrays and `S` is a 1D list or numpy array. The function should use standard libraries or packages available in Python for matrix operations and SVD computation.
"""

import numpy as np

def partial_svd(matrix, num_singular_values):
    U, S, V = np.linalg.svd(matrix, full_matrices=False)
    U = U[:, :num_singular_values]
    S = S[:num_singular_values]
    V = V[:num_singular_values, :]
    return U, S, V