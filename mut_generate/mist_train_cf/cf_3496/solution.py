"""
QUESTION:
Create a function named `cosine_similarity` that takes two lists of numeric values, `vector1` and `vector2`, as input, calculates the cosine similarity between them, and returns the result. The cosine similarity is defined as the dot product of the two vectors divided by the product of their magnitudes. The input vectors have the same length and can have a maximum length of 10^6. Handle this efficiently in the code.
"""

import math

def cosine_similarity(vector1, vector2):
    """
    Calculate the cosine similarity between two vectors.
    
    Parameters:
    vector1 (list): The first vector.
    vector2 (list): The second vector.
    
    Returns:
    float: The cosine similarity between the two vectors.
    """
    dot_product = 0
    magnitude1 = 0
    magnitude2 = 0

    # Calculate dot product and magnitude of each vector
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
        magnitude1 += vector1[i] ** 2
        magnitude2 += vector2[i] ** 2

    # Calculate magnitudes
    magnitude1 = math.sqrt(magnitude1)
    magnitude2 = math.sqrt(magnitude2)

    # Calculate cosine similarity
    cosine_similarity = dot_product / (magnitude1 * magnitude2)

    return cosine_similarity