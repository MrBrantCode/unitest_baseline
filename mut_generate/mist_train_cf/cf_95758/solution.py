"""
QUESTION:
Implement a function `vector_angle(a, b)` to find the angle between two given 3D vectors `a` and `b` using only basic mathematical operations. The function should have a time complexity of O(1), handle edge cases such as zero vectors or parallel vectors, and not use any trigonometric functions or pre-built vector/matrix libraries. Return the angle in degrees.
"""

import math

def vector_angle(a, b):
    dotProduct = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    length_a = math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
    length_b = math.sqrt(b[0] ** 2 + b[1] ** 2 + b[2] ** 2)
    lengthProduct = length_a * length_b
    
    # Check for edge cases: zero vectors or parallel vectors
    if lengthProduct == 0:
        return "Error: Zero vector detected"
    elif dotProduct == lengthProduct:
        return 0
    
    cosine = dotProduct / lengthProduct
    angle = math.acos(cosine)
    
    return math.degrees(angle)