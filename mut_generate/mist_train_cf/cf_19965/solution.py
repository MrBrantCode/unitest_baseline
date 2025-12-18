"""
QUESTION:
Create a function `calculate_surface_area_cylinder(radius, height)` that calculates the surface area of a cylinder given the radius and height, without using the built-in mathematical functions for pi and exponentiation. The function should only use basic mathematical operations, handle both positive and negative values for radius and height inputs, and round the surface area to 2 decimal places. If either the radius or height is negative, the function should return an error message.
"""

import math

def calculate_surface_area_cylinder(radius, height):
    """
    Calculates the surface area of a cylinder given the radius and height.

    Args:
        radius (float): The radius of the cylinder.
        height (float): The height of the cylinder.

    Returns:
        float: The surface area of the cylinder rounded to 2 decimal places.
        str: An error message if either the radius or height is negative.
    """
    if radius < 0 or height < 0:
        return "Invalid input: radius and height must be positive values."
    
    # Using 22/7 as an approximation for pi
    pi_approximation = 22 / 7
    
    surface_area = 2 * pi_approximation * radius * (radius + height)
    
    return round(surface_area, 2)