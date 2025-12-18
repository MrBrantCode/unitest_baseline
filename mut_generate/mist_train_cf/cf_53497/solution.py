"""
QUESTION:
Calculate the area of a triangle with side lengths a, b, and c using Heron's formula, given that a + b > c, a + c > b, and b + c > a. Implement a function `calculate_area(a, b, c)` that takes the three side lengths as input and returns the area of the triangle.
"""

import math

def calculate_area(a, b, c):
    # Calculating semi perimeter
    s = (a + b + c) / 2

    # Use Heron's formula to calculate area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area