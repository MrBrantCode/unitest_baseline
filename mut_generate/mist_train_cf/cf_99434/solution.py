"""
QUESTION:
Calculate the area of a triangle given its three side lengths using Heron's formula. Implement a function named `calculate_triangle_area` that takes three side lengths as input and returns the calculated area. The function should use Heron's formula, which states that the area of a triangle with sides a, b, and c is given by `s = (a + b + c) / 2` and `area = √(s(s-a)(s-b)(s-c))`.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        float: The area of the triangle.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))