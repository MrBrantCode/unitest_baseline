"""
QUESTION:
Write a function named `calculate_sphere_volume` that calculates the volume of a sphere given its radius using the formula V = (4/3) * π * r³, where π is a mathematical constant approximately equal to 3.14159 and r is the radius of the sphere. The function should take one parameter, the radius of the sphere, and return the calculated volume.
"""

import math

def calculate_sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The calculated volume of the sphere.
    """
    return (4/3) * math.pi * radius**3