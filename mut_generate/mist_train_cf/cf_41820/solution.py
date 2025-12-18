"""
QUESTION:
Implement a function `calculate_coherence` that takes a 2D numpy array `mat` as input and returns the coherence of the matrix as a float. The coherence is defined as the maximum absolute value of the normalized inner products of its distinct columns. The input matrix `mat` has shape (N, M), where N is the number of rows and M is the number of columns.
"""

import numpy as np

def calculate_coherence(mat: np.ndarray) -> float:
    """
    Calculate the coherence of the input matrix.

    Parameters
    ----------
    mat : (N, M) np.ndarray
        The input matrix :math:`\boldsymbol{A}`.

    Returns
    -------
    float
        Coherence value of the input matrix.
    """
    num_cols = mat.shape[1]
    max_coherence = 0.0

    for i in range(num_cols):
        for j in range(i + 1, num_cols):
            col_i = mat[:, i]
            col_j = mat[:, j]
            inner_product = np.abs(np.dot(col_i, col_j))
            norm_product = np.linalg.norm(col_i) * np.linalg.norm(col_j)
            coherence_ij = inner_product / norm_product
            max_coherence = max(max_coherence, coherence_ij)

    return max_coherence