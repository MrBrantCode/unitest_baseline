"""
QUESTION:
Write a function named calculate_circle_area that calculates the area of a circle given its radius. The function should return the area in squared centimeters.
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
    radius (float): The radius of the circle in centimeters.

    Returns:
    float: The area of the circle in squared centimeters.
    """
    return math.pi * (radius ** 2)