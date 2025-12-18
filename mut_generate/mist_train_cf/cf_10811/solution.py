"""
QUESTION:
Write a function named `cosine_similarity` that takes two vectors as input and returns the cosine similarity of the vectors. The cosine similarity is calculated using the formula: (A · B) / (||A|| * ||B||), where A · B is the dot product of vectors A and B, and ||A|| and ||B|| are the magnitudes of vectors A and B, respectively.
"""

import math

def cosine_similarity(vector1, vector2):
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(x ** 2 for x in vector2))
    return dot_product / (magnitude1 * magnitude2)