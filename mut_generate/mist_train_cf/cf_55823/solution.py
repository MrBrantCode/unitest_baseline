"""
QUESTION:
Write a function named `calculate_ellipse_circumference` that takes the semi-major axis `a` and semi-minor axis `b` as input and returns an approximation of the circumference of an ellipse using Ramanujan's formula. The function should use the math library for the square root and pi calculations.
"""

import math

def calculate_ellipse_circumference(a, b):
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))