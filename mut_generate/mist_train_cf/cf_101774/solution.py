"""
QUESTION:
Write a function named `calculate_triangle_area` that calculates the area of a triangle given its side lengths. The function should take three parameters: `a`, `b`, and `c`, representing the lengths of the sides of the triangle. The function should return the area of the triangle.

Note that the function should be able to handle triangles with sides of different lengths, and it should use Heron's formula to calculate the area.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle given its side lengths.

    Parameters:
    a (float): The length of side a.
    b (float): The length of side b.
    c (float): The length of side c.

    Returns:
    float: The area of the triangle.
    """
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area