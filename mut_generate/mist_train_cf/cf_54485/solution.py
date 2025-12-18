"""
QUESTION:
Write a function `triangle_area` that takes the lengths of two sides of a triangle (`a` and `b`) and the included angle in degrees (`angle`) as input, and returns the area of the triangle.
"""

import math

def triangle_area(a, b, angle):
    """
    Calculate the area of a triangle given two sides and the included angle.

    Args:
        a (float): The length of the first side.
        b (float): The length of the second side.
        angle (float): The included angle in degrees.

    Returns:
        float: The area of the triangle.
    """
    # Convert the angle from degrees to radians for the math.sin function
    angle_rad = math.radians(angle)
    # Calculate the area using the formula: 0.5 * a * b * sin(C)
    area = 0.5 * a * b * math.sin(angle_rad)
    return area