"""
QUESTION:
Write a function `total_interior_surface_area` that calculates the total interior surface area of a cylindrical tube given its height, outer radius, and inner radius, and returns the result. The function should take three parameters: `height`, `outer_radius`, and `inner_radius`, all of which are in centimeters. Note that the outer radius is not used in the calculation.
"""

import math

def total_interior_surface_area(height, outer_radius, inner_radius):
    """
    Calculate the total interior surface area of a cylindrical tube.

    Parameters:
    height (float): Height of the tube in centimeters.
    outer_radius (float): Outer radius of the tube in centimeters.
    inner_radius (float): Inner radius of the tube in centimeters.

    Returns:
    float: The total interior surface area of the cylindrical tube in square centimeters.
    """
    lateral_area = 2 * math.pi * inner_radius * height
    base_area = 2 * math.pi * inner_radius ** 2
    return lateral_area + base_area