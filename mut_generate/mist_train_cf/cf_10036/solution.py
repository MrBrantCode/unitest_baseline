"""
QUESTION:
Write a function `calculate_circle_area` that takes a string representing the radius of a circle as input and returns the area of the circle as a floating-point number. The function should convert the input string to a numeric value and use the formula `π * r^2` to calculate the area.
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given the radius.

    Args:
        radius (str): The radius of the circle as a string.

    Returns:
        float: The area of the circle.
    """
    radius = float(radius)
    return math.pi * radius**2