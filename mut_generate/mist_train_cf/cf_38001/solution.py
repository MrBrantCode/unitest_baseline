"""
QUESTION:
Implement a function `calculate_cosine_similarity` that calculates the cosine similarity between two non-zero vectors represented as numpy arrays. The function should take two parameters, `vector_a` and `vector_b`, and return the cosine similarity as a float value. The cosine similarity is calculated using the formula: (A . B) / (||A|| * ||B||), where A . B represents the dot product of A and B, and ||A|| and ||B|| represent the Euclidean norms of A and B respectively.
"""

import numpy as np

def calculate_cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    cosine_similarity = dot_product / (norm_a * norm_b)
    return cosine_similarity