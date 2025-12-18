"""
QUESTION:
Write a function named `calculate_triangle_properties` that takes the lengths of the sides of a triangle as input and returns the area and inradius of the triangle using Heron's formula. The input should be three numbers representing the sides of the triangle and the output should be two numbers representing the area and inradius, respectively.
"""

import math

def calculate_triangle_properties(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Calculate the inradius
    inradius = area / s
    return area, inradius