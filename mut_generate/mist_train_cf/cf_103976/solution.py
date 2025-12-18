"""
QUESTION:
Write a function called `cosine_distance` that calculates the cosine distance between two input vectors. The function should take two lists of numbers as input, representing the vectors, and return the cosine distance between them. The cosine distance is calculated using the formula: 1 - (dot_product(vector1, vector2) / (magnitude(vector1) * magnitude(vector2))), where dot_product is the sum of the products of corresponding elements and magnitude is the square root of the sum of the squares of the elements.
"""

import math

def cosine_distance(vector1, vector2):
    def dot_product(vector1, vector2):
        return sum(x * y for x, y in zip(vector1, vector2))

    def magnitude(vector):
        return math.sqrt(sum(x ** 2 for x in vector))

    dot = dot_product(vector1, vector2)
    mag1 = magnitude(vector1)
    mag2 = magnitude(vector2)
    return 1 - (dot / (mag1 * mag2))