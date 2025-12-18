"""
QUESTION:
Write a function named `cosine_similarity` that takes two vectors as input and returns their cosine similarity. The function should be able to handle vectors with lengths up to 1 million and containing floating-point numbers ranging from -100 to 100. The cosine similarity is calculated using the formula: `cosine_similarity = dot_product / (magnitude_vector1 * magnitude_vector2)`.
"""

import numpy as np

def cosine_similarity(vector1, vector2):
    # Convert the vectors to numpy arrays
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    # Compute the dot product of the vectors
    dot_product = np.dot(vector1, vector2)

    # Compute the magnitude of the vectors
    magnitude_vector1 = np.linalg.norm(vector1)
    magnitude_vector2 = np.linalg.norm(vector2)

    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_vector1 * magnitude_vector2)

    return cosine_similarity