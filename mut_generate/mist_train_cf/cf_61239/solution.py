"""
QUESTION:
Create a function `calculate_cone_volume` that calculates the volume of a cone given its radius and height. The function should return the volume of the cone in cubic meters, rounded to two decimal places. The formula for the volume of a cone is V = 1/3 * π * r² * h, where r is the radius and h is the height of the cone.
"""

import math

def calculate_cone_volume(radius, height):
    """
    Calculates the volume of a cone given its radius and height.

    Args:
        radius (float): The radius of the cone in meters.
        height (float): The height of the cone in meters.

    Returns:
        float: The volume of the cone in cubic meters, rounded to two decimal places.
    """
    volume = (1/3) * math.pi * (radius ** 2) * height
    return round(volume, 2)