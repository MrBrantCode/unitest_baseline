"""
QUESTION:
Write a function `calculate_cosine_similarity` that takes a list of sparse vectors as input, where each sparse vector is a list of tuples representing indices and values of non-zero elements. The function should return a list of tuples, where each tuple contains the indices of two sparse vectors and their cosine similarity. The function should calculate the cosine similarity between each pair of vectors and return the results in a list. The cosine similarity is defined as the dot product of two vectors divided by the product of their magnitudes.
"""

import numpy as np

def calculate_cosine_similarity(sparse_vectors):
    def dot_product(v1, v2):
        result = 0.0
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if v1[i][0] == v2[j][0]:
                result += v1[i][1] * v2[j][1]
                i += 1
                j += 1
            elif v1[i][0] < v2[j][0]:
                i += 1
            else:
                j += 1
        return result

    def magnitude(v):
        return np.sqrt(sum(val ** 2 for (_, val) in v))

    similarities = []
    for i in range(len(sparse_vectors)):
        for j in range(i + 1, len(sparse_vectors)):
            v1, v2 = sparse_vectors[i], sparse_vectors[j]
            dot = dot_product(v1, v2)
            mag = magnitude(v1) * magnitude(v2)
            similarity = dot / mag if mag != 0 else 0.0
            similarities.append(((i, j), similarity))
    return similarities