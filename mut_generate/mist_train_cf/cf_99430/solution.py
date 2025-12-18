"""
QUESTION:
Write a function named equilateral_triangle_height that calculates the height of an equilateral triangle given the length of one side. The function should take one argument s, the length of one side of the triangle, and return the calculated height. The function should use the formula h = (sqrt(3) / 2) * s, where h is the height of the triangle and sqrt(3) is the square root of 3.
"""

import math

def equilateral_triangle_height(s):
    """
    Calculates the height of an equilateral triangle given the length of one side.

    Args:
        s (float): The length of one side of the triangle.

    Returns:
        float: The calculated height of the triangle.
    """
    return (math.sqrt(3) / 2) * s