"""
QUESTION:
Write a function `parallelogram_area` that calculates the area of a parallelogram given the lengths of two adjacent sides and the angle between them. The function should take three parameters: `a` and `b`, representing the lengths of the two adjacent sides, and `C`, representing the angle between the sides in degrees. The function should return the calculated area.
"""

import math

def parallelogram_area(a, b, C):
    # Convert angle from degrees to radians
    C_rad = math.radians(C)
    # Calculate the area using the formula
    area = a * b * math.sin(C_rad)
    return area