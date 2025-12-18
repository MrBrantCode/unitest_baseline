"""
QUESTION:
Create a function called `calculate_sphere_properties` that takes in a radius and density as parameters and returns the surface area and mass of a sphere. The surface area should be calculated using the formula 4πr², and the mass should be calculated using the formula (4/3)πr³ times the density. The function should return the results as a formatted string with two decimal places for both values.
"""

import math

def calculate_sphere_properties(radius, density):
    """
    Calculate the surface area and mass of a sphere.

    Args:
        radius (float): The radius of the sphere.
        density (float): The density of the sphere.

    Returns:
        str: A formatted string containing the surface area and mass of the sphere.
    """
    surface_area = 4 * math.pi * radius ** 2
    mass = density * (4/3) * math.pi * radius ** 3
    return "Surface area: {:.2f} cm², Mass: {:.2f} g".format(surface_area, mass)