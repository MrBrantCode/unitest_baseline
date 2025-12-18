"""
QUESTION:
Write a function `triangle_area_law_of_cosines` that takes in the lengths of two sides of a triangle (`a` and `b`) and the angle opposite to the third side (`angle_C` in degrees) as arguments. The function should return the area of the triangle using the Law of Cosines.
"""

import math

def triangle_area_law_of_cosines(a, b, angle_C):
    angle_C = math.radians(angle_C)
    cos_C = math.cos(angle_C)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * cos_C)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area