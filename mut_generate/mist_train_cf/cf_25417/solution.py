"""
QUESTION:
Write a function `calculate_circle_area` that calculates the area of a circle given its radius. The function should take the radius as an argument and return the calculated area. The area should be calculated using the formula πr^2, where π is approximately 3.14.
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The calculated area of the circle.
    """
    return math.pi * (radius ** 2)