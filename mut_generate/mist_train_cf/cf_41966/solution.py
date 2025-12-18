"""
QUESTION:
Write a function `truncated_svd(A, k)` that takes an m x n matrix `A` and an integer `k` as input, performs a truncated Singular Value Decomposition (SVD) on the matrix `A`, and returns the reconstructed matrix using the first `k` singular values. The reconstructed matrix should be approximately equal to `A ≈ UΣV^T`, where `U` is an `m x k` matrix, `Σ` is a `k x k` diagonal matrix, and `V^T` is a `k x n` matrix, with the diagonal elements of `Σ` being the singular values of `A` in descending order.
"""

from typing import List
import numpy as np

def entrance(A: List[List[float]], k: int) -> List[List[float]]:
    A = np.array(A)
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    reconstructed_A = np.dot(U[:, :k] * S[:k], Vt[:k, :])
    return reconstructed_A.tolist()