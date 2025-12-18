"""
QUESTION:
Write a function named `angle_between_vectors` that calculates the angle in degrees between two given three-dimensional vectors without using trigonometric functions in the calculation itself. The function should take two vectors as input and return the angle in degrees. The time complexity of the function should be O(1).
"""

import math

def angle_between_vectors(vector_A, vector_B):
    dot_product = sum(a * b for a, b in zip(vector_A, vector_B))
    magnitude_A = math.sqrt(sum(a * a for a in vector_A))
    magnitude_B = math.sqrt(sum(b * b for b in vector_B))
    cosine_theta = dot_product / (magnitude_A * magnitude_B)
    return math.acos(cosine_theta)