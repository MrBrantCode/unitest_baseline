"""
QUESTION:
Write a function `angle_between_vectors(vector_A, vector_B)` that takes two 3D vectors `vector_A` and `vector_B` as input and returns the angle between them in degrees. The function should use the dot product formula and not use any trigonometric functions in its calculations. The time complexity of the function should be O(1).
"""

import math

def angle_between_vectors(vector_A, vector_B):
    dot_product = sum(a * b for a, b in zip(vector_A, vector_B))
    magnitude_A = math.sqrt(sum(a * a for a in vector_A))
    magnitude_B = math.sqrt(sum(b * b for b in vector_B))
    cosine_theta = dot_product / (magnitude_A * magnitude_B)
    theta = math.acos(cosine_theta)
    return math.degrees(theta)