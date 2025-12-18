"""
QUESTION:
Write a function called `triangle_area` that takes a list of three integers representing the side lengths of a triangle as input and returns the area of the triangle using Heron's formula. The input list will always contain three positive integers.
"""

import math

def triangle_area(sides):
    """
    Calculate the area of a triangle using Heron's formula.

    Args:
        sides (list): A list of three integers representing the side lengths of a triangle.

    Returns:
        float: The area of the triangle.
    """
    a, b, c = sides
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))