"""
QUESTION:
Write a function called `triangle_height` that calculates the height of a triangle given the length of its base side (b) and the angle opposite the height (A). The angle should be passed in degrees and the function should return the height of the triangle in the same units as the base side. Assume the input values are valid and the triangle is not a right triangle.
"""

import math

def triangle_height(b, A):
    # angle should be in radians for the math.sin function
    A = math.radians(A)
    h = b * math.sin(A)
    return h