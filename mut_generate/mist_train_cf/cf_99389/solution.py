"""
QUESTION:
Write a Python function `calculate_triangle_area` that takes as input three side lengths `a`, `b`, and `c` of a triangle and returns the area of the triangle using Heron's formula. The function should also be able to handle different side lengths. Additionally, write alternative functions `calculate_triangle_area_by_height` and `calculate_triangle_area_by_circumradius` that calculate the area of a triangle given the base and height, and the side lengths and circumradius, respectively.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle given its side lengths using Heron's formula.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        float: The area of the triangle.
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calculate_triangle_area_by_height(base, height):
    """
    Calculate the area of a triangle given its base and height.

    Args:
        base (float): The length of the base.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    area = (base * height) / 2
    return area

def calculate_triangle_area_by_circumradius(a, b, c, R):
    """
    Calculate the area of a triangle given its side lengths and circumradius.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.
        R (float): The circumradius of the triangle.

    Returns:
        float: The area of the triangle.
    """
    area = (a * b * c) / (4 * R)
    return area