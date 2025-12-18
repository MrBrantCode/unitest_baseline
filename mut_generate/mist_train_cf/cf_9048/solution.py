"""
QUESTION:
Create a function called `find_triangle_area` that takes four arguments: `base`, `height`, and the lengths of the three sides of a triangle `side1`, `side2`, `side3`. The function should return the total area of the triangle using Heron's formula.
"""

import math

def find_triangle_area(base, height, side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area