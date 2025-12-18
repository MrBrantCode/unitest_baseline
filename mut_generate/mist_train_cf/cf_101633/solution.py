"""
QUESTION:
Write a Python function named `calculate_sphere_properties` that calculates the surface area and mass of a sphere given its radius and density. The surface area should be calculated using the formula 4πr², and the mass should be calculated by multiplying the volume of the sphere (4/3)πr³ by the density. The function should return a formatted string containing the surface area in cm² and the mass in grams, rounded to two decimal places.
"""

import math

def calculate_sphere_properties(radius, density):
    """
    Calculate the surface area and mass of a sphere given its radius and density.

    Args:
        radius (float): The radius of the sphere in cm.
        density (float): The density of the sphere in g/cm³.

    Returns:
        str: A formatted string containing the surface area in cm² and the mass in grams.
    """
    surface_area = 4 * math.pi * radius ** 2
    mass = density * (4/3) * math.pi * radius ** 3
    return "Surface area: {:.2f} cm²\nMass: {:.2f} g".format(surface_area, mass)