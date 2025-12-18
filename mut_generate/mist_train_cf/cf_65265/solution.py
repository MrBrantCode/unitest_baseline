"""
QUESTION:
Write a function called `calculate_inscribed_circle_area` that takes the length and width of a rectangle as parameters and returns the area of the largest circle that can be inscribed within the rectangle.
"""

import math

def calculate_inscribed_circle_area(length, width):
    """
    Calculate the area of the largest circle that can be inscribed within a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the inscribed circle.
    """
    # The diameter of the inscribed circle is equal to the shorter side of the rectangle
    diameter = min(length, width)
    
    # The radius is half the diameter
    radius = diameter / 2
    
    # The area of a circle is pi times the radius squared
    area = math.pi * (radius ** 2)
    
    return area