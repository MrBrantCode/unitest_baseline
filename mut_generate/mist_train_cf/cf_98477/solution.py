"""
QUESTION:
Write a function `calculate_triangle_area` that calculates the area of a triangle given the lengths of its three sides using Heron's formula. The function should take in three parameters, a, b, and c, representing the lengths of the sides, and return the area of the triangle.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides using Heron's formula.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        float: The area of the triangle.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))