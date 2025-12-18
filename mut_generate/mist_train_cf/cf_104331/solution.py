"""
QUESTION:
Write a function named `cosine_similarity` that takes two vectors of equal length as input and returns their cosine similarity. The function should calculate the cosine similarity as the dot product of the vectors divided by the product of their magnitudes, where the magnitude of a vector is the square root of the sum of the squares of its elements.
"""

import math

def cosine_similarity(vector1, vector2):
    """
    Calculate the cosine similarity of two vectors.

    Args:
    vector1 (list): The first vector.
    vector2 (list): The second vector.

    Returns:
    float: The cosine similarity of the two vectors.
    """
    
    # Calculate the dot product of the two vectors
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    
    # Calculate the magnitudes of the two vectors
    magnitude1 = math.sqrt(sum(a ** 2 for a in vector1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vector2))
    
    # Calculate the cosine similarity
    return dot_product / (magnitude1 * magnitude2)