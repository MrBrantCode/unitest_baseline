"""
QUESTION:
Write a function `calculate_surface_area` that calculates the surface area of a cylinder given its radius and height, where both radius and height are positive numbers. The surface area should be calculated using the formula `2 * pi * radius * (radius + height)`. The function should take two parameters `radius` and `height` and return the calculated surface area.
"""

import math

def calculate_surface_area(radius, height):
    """
    Calculate the surface area of a cylinder.

    Args:
    radius (float): The radius of the cylinder.
    height (float): The height of the cylinder.

    Returns:
    float: The surface area of the cylinder.
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area