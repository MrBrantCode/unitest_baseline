"""
QUESTION:
Calculate the surface area of a sphere given the radius. Create a function `sphere_surface_area` that takes the radius as an argument and returns the calculated surface area. The function should use the formula 4 * π * radius^2 to calculate the surface area.
"""

import math

def sphere_surface_area(radius):
    """
    Calculate the surface area of a sphere given the radius.
    
    Parameters:
    radius (float): The radius of the sphere.
    
    Returns:
    float: The surface area of the sphere.
    """
    return 4 * math.pi * radius ** 2