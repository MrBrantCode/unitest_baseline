"""
QUESTION:
Write a function named `sphere_volume` that calculates the volume of a sphere given its radius. The function should take one argument, the radius of the sphere, and return the volume. The formula for the volume of a sphere is (4/3) * π * r^3, where r is the radius of the sphere.
"""

import math

def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    return (4/3) * math.pi * (radius ** 3)