"""
QUESTION:
Implement a function `orthonormalize` that takes a 2D numpy array `vectors` of shape (m, n) representing a set of linearly independent vectors, an integer `num_orthonormals` specifying the number of orthonormalized vectors to return (default is 1), and a small positive float `eps` representing the tolerance for considering a vector as zero (default is 1e-6). The function should return a 2D numpy array of shape (m, num_orthonormals) containing the orthonormalized vectors obtained using the Gram-Schmidt process. Assume the input vectors are not all zero vectors.
"""

import numpy as np

def orthonormalize(vectors, num_orthonormals=1, eps=1e-6):
    q, _ = np.linalg.qr(vectors)
    orthonormalized = q[:, :num_orthonormals]
    return orthonormalized