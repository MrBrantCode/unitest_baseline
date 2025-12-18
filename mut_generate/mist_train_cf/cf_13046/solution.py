"""
QUESTION:
Create a function named `circle_properties` to calculate and return the area and circumference of a circle given its radius. The function should take one argument `radius` and return the area and circumference as floats, rounded to two decimal places. The input radius is expected to be a non-negative number.
"""

import math

def circle_properties(radius):
    """
    Calculate and return the area and circumference of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        tuple: A tuple containing the area and circumference of the circle, rounded to two decimal places.
    """
    area = round(math.pi * (radius ** 2), 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference