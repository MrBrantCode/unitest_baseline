"""
QUESTION:
Write a function `cosine_similarity(A, B)` that calculates the cosine similarity between two vectors A and B, defined as the dot product of A and B divided by the product of their magnitudes, and returns the result as a floating-point number rounded to 4 decimal places. The input vectors A and B are 1D NumPy arrays.
"""

import numpy as np

def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    magnitude_A = np.linalg.norm(A)
    magnitude_B = np.linalg.norm(B)
    similarity = dot_product / (magnitude_A * magnitude_B)
    return round(similarity, 4)