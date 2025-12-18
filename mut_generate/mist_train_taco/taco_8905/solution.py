"""
QUESTION:
Write function heron which calculates the area of a triangle with sides a, b, and c.

Heron's formula: sqrt (s \* (s - a) \* (s - b) \* (s - c)), where s = (a + b + c) / 2.
Output should have 2 digits precision.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Parameters:
    a (float): The length of the first side of the triangle.
    b (float): The length of the second side of the triangle.
    c (float): The length of the third side of the triangle.

    Returns:
    float: The area of the triangle, rounded to 2 decimal places.
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)