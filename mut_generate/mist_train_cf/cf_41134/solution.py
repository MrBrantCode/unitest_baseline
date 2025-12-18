"""
QUESTION:
Write a function `calculate_similarity(x, w)` that calculates the cosine similarity between each pair of vectors in `x` and `w`. The input arrays `x` and `w` have shapes `[batch_size, vector_dimension]` and `[vector_dimension, out_planes]` respectively. The function should return a 2D array of shape `[batch_size, out_planes]`, where each element at index `[i, j]` represents the cosine similarity between the `i`-th vector in `x` and the `j`-th vector in `w`. The cosine similarity between two vectors `a` and `b` is defined as the dot product of the two vectors divided by the product of their magnitudes.
"""

import numpy as np

def calculate_similarity(x, w):
    x_modulus = np.sqrt(np.sum(np.power(x, 2), axis=1))  # Magnitude of each vector in x
    w_modulus = np.sqrt(np.sum(np.power(w, 2), axis=0))  # Magnitude of each vector in w

    dot_product = np.dot(x, w)  # Dot product of x and w
    cosine_sim = dot_product / np.outer(x_modulus, w_modulus)  # Cosine similarity calculation

    return cosine_sim