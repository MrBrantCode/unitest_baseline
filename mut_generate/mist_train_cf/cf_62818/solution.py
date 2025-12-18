"""
QUESTION:
Create a function named `calculate_area` that takes the lengths of the sides of a triangle (a, b, c) as input and returns the area of the triangle using Heron's formula. The function should assume the inputs are valid (i.e., a, b, and c can form a triangle) and should not perform any error checking. The triangle is assumed to be acute (all angles less than 90 degrees).
"""

import math

def calculate_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area