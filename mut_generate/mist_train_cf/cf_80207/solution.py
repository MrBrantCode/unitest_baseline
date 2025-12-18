"""
QUESTION:
Write a function named `sphere_volume` that takes the radius of a sphere as input and returns its volume, calculated using the formula V = 4/3 * π * r^3. The radius will be provided in centimeters, and the volume should be returned in cubic centimeters.
"""

import math

def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere in centimeters.

    Returns:
        float: The volume of the sphere in cubic centimeters.
    """
    return (4/3) * math.pi * (radius**3)