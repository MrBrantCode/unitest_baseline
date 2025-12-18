"""
QUESTION:
Create a function named `calculate_area` that calculates the area of a triangle given the lengths of its three sides. The function should take three parameters `a`, `b`, and `c`, representing the side lengths, and return the calculated area.
"""

import math

def calculate_area(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area