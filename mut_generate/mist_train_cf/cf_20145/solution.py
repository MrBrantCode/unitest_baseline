"""
QUESTION:
Write a function named `calculate_circle_properties` that takes the radius of a circle as a decimal number rounded to the nearest thousandth and returns its area and circumference.
"""

import math

def calculate_circle_properties(radius):
    """
    Calculate the area and circumference of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle, rounded to the nearest thousandth.
    
    Returns:
        tuple: A tuple containing the area and circumference of the circle.
    """
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference