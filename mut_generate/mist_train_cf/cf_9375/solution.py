"""
QUESTION:
Calculate the area of a circle given its radius. The radius can be any positive real number. Implement a function named `calculate_circle_area` to calculate and return the area rounded to two decimal places.
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle rounded to two decimal places.
    """
    area = math.pi * (radius ** 2)
    return round(area, 2)