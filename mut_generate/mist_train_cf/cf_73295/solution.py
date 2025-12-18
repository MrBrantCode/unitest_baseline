"""
QUESTION:
Calculate the internal surface area of a cylinder given its internal radius and height. 

Create a function called `calculate_internal_surface_area` that takes two parameters: `height` and `internal_radius`, both in centimeters, and returns the internal surface area in square centimeters. The function should use the formula 2 * π * r * h.
"""

import math

def calculate_internal_surface_area(height, internal_radius):
    """
    Calculate the internal surface area of a cylinder.

    Parameters:
    height (float): The height of the cylinder in centimeters.
    internal_radius (float): The internal radius of the cylinder in centimeters.

    Returns:
    float: The internal surface area of the cylinder in square centimeters.
    """
    return 2 * math.pi * internal_radius * height