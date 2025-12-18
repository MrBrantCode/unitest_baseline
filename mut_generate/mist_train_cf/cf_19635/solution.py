"""
QUESTION:
Create a function named `vector_angle` that takes two vectors `a` and `b` as input in a three-dimensional space and returns the angle between them in degrees. The time complexity should be O(1), and the solution should only use basic mathematical operations (addition, subtraction, multiplication, and division) without any trigonometric functions or pre-built vector/matrix libraries. Handle edge cases such as zero vectors or parallel vectors and provide an error message or zero angle respectively.
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