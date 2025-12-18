"""
QUESTION:
Write a function `triangle_area` that takes three parameters, the lengths of the sides of a triangle, and returns the area of the triangle. The function should use Heron's formula and handle cases where the input lengths do not form a valid triangle.
"""

import math

def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    if s * (s - side1) * (s - side2) * (s - side3) < 0:
        return "Invalid input: The input lengths do not form a valid triangle."
    else:
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))