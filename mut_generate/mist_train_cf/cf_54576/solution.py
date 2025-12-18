"""
QUESTION:
Create a function `calc_volume` that calculates the volume of a cylinder given its height and diameter. The function should take two arguments: `height` and `diameter`, both floating point numbers between 1 and 100. The function should return the volume of the cylinder, rounded to two decimal places.

The function should also be used to calculate the volume of 1000 unique, randomly generated cylinders with heights and diameters between 1 and 100, and return the height, diameter, and volume of the cylinder with the largest volume. The function should be optimized for efficient execution.
"""

import math

def calc_volume(height, diameter):
    """
    Calculate the volume of a cylinder given its height and diameter.

    Args:
        height (float): The height of the cylinder (between 1 and 100).
        diameter (float): The diameter of the cylinder (between 1 and 100).

    Returns:
        float: The volume of the cylinder, rounded to two decimal places.
    """
    radius = diameter / 2
    return round(math.pi * radius**2 * height, 2)