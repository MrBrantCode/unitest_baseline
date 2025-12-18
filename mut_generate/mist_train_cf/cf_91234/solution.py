"""
QUESTION:
Create a function `triangle_area_law_of_cosines` that takes in three arguments: the lengths of two sides of a triangle (`a` and `b`) and the angle opposite to the third side (`angle_C` in degrees). Using the Law of Cosines and Heron's formula, calculate and return the area of the triangle.
"""

import math

def triangle_area_law_of_cosines(a, b, angle_C):
    # Convert the angle to radians
    angle_C = math.radians(angle_C)

    # Calculate the cosine of the given angle
    cos_C = math.cos(angle_C)

    # Calculate the length of the third side using the Law of Cosines
    c = math.sqrt(a**2 + b**2 - 2 * a * b * cos_C)

    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area