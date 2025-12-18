"""
QUESTION:
Implement a function `angle_between_vectors(v1, v2)` that calculates the angle between two given vectors `v1` and `v2` in a 3D space, returning the angle in degrees. The function should handle edge cases, including null vectors and vectors with negative coordinates, and should not rely on built-in mathematical vector operations.
"""

import math

def angle_between_vectors(v1, v2):
    # handle null vectors
    if math.sqrt(sum(i**2 for i in v1)) == 0 or math.sqrt(sum(i**2 for i in v2)) == 0:
        return None

    # Calculate dot product
    dot_prod = sum(a*b for a, b in zip(v1, v2))

    # Calculate lengths
    len_v1 = math.sqrt(sum(i**2 for i in v1))
    len_v2 = math.sqrt(sum(i**2 for i in v2))

    # Calculate the cosine of the angle
    cos_angle = dot_prod / (len_v1 * len_v2)

    # Handle floating point precision issues
    if cos_angle > 1.0:
        cos_angle = 1.0
    elif cos_angle < -1.0:
        cos_angle = -1.0

    # Return the angle in degrees
    return math.degrees(math.acos(cos_angle))