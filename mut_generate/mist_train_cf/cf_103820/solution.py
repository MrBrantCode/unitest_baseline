"""
QUESTION:
Create a function `calculate_area` that takes the lengths of the three sides of a triangle as input and returns its area calculated using Heron's formula. The input values are floating point numbers and the function should return a floating point number representing the area.
"""

import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area