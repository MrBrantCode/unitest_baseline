"""
QUESTION:
Implement a function called `gram_schmidt_process` that applies the Gram-Schmidt process to transform a set of vectors into an orthogonal set. The function should take a 2D list `A` representing a matrix where each column is a feature vector, and return the orthogonal matrix `Q`. The vectors in `Q` should be normalized to have a length of 1. Assume the input matrix `A` has linearly independent columns.
"""

import numpy as np

def gram_schmidt_process(A):
    """
    Applies the Gram-Schmidt process to transform a set of vectors into an orthogonal set.

    Parameters:
    A (2D list): A matrix where each column is a feature vector.

    Returns:
    Q (2D list): The orthogonal matrix where the vectors are normalized to have a length of 1.
    """
    Q = np.zeros_like(A, dtype=float)
    for i, v in enumerate(A.T):
        # subtract the projection of v on each of the already calculated vectors in Q
        for j in range(i):
            q = Q[:, j]
            v = v - np.dot(v, q) * q
        # normalize the result and assign it to the corresponding column in Q
        Q[:, i] = v / np.linalg.norm(v)
    return Q