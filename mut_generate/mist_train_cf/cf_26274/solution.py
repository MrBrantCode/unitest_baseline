"""
QUESTION:
Write a function named cosine_distance that calculates the cosine distance between two input vectors. The function should take two parameters, a and b, representing the vectors. The cosine distance is defined as 1 - (a · b) / (|a| |b|), where a · b is the dot product of a and b, and |a| and |b| are the magnitudes (Euclidean norms) of a and b. Ensure the function returns the calculated cosine distance value.
"""

import math

def cosine_distance(a, b):
    """
    Calculate the cosine distance between two input vectors.

    Args:
        a (list): The first vector.
        b (list): The second vector.

    Returns:
        float: The cosine distance between the two vectors.
    """
    numerator = sum(x * y for x, y in zip(a, b))
    denominator = math.sqrt(sum(x ** 2 for x in a)) * math.sqrt(sum(y ** 2 for y in b))
    return 1 - (numerator / denominator)