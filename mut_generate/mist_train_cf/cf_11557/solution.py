"""
QUESTION:
Write a function called `calculate_sphere_volume` that takes the radius of a sphere as input and returns its volume using the formula V = (4/3)πr^3. The function should return the volume as a float value.
"""

import math

def calculate_sphere_volume(radius: float) -> float:
    """
    Calculate the volume of a sphere given its radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """
    return (4/3) * math.pi * (radius ** 3)