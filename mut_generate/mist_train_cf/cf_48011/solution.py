"""
QUESTION:
Write a function named `calculate_sphere_properties` that takes the radius of a sphere as input and returns the surface area and volume of the sphere. The surface area should be calculated using the formula 4πr² and the volume using the formula 4/3πr³.
"""

import math

def calculate_sphere_properties(radius):
    """
    Calculate the surface area and volume of a sphere.

    Args:
    radius (float): The radius of the sphere.

    Returns:
    tuple: A tuple containing the surface area and volume of the sphere.
    """
    surface_area = 4 * math.pi * (radius ** 2)
    volume = (4/3) * math.pi * (radius ** 3)
    return surface_area, volume