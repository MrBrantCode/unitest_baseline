"""
QUESTION:
Write a function named calculate_circumference that takes the area of a circle as input and returns its circumference. The function should use the formulas A = πr² and C = 2πr to calculate the circumference, where A is the area, C is the circumference, and r is the radius. Assume π is approximately 3.14159.
"""

import math

def calculate_circumference(area):
    """
    Calculate the circumference of a circle given its area.

    Args:
        area (float): The area of the circle.

    Returns:
        float: The circumference of the circle.
    """
    radius = math.sqrt(area / math.pi)
    circumference = 2 * math.pi * radius
    return circumference