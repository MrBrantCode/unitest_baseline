"""
QUESTION:
Write a function named `calculate_circle_area` that takes a radius as input and returns the area of the corresponding circle. The area should be calculated using the formula πr², where π is approximately 3.14159.
"""

import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * math.pow(radius, 2)