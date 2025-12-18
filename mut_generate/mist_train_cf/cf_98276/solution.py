"""
QUESTION:
Write a function called `triangle_properties` that takes the lengths of the three sides of a triangle as input and returns the area and inradius of the triangle using Heron's formula. The function should take three parameters, a, b, and c, representing the lengths of the sides.
"""

import math

def triangle_properties(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s
    return area, inradius