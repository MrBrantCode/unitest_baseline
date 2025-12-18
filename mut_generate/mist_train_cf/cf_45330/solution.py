"""
QUESTION:
Create a function named `calculate_surface_area` that calculates the surface area of a circle given its radius. The surface area should be calculated using the formula A = πr².
"""

import math

def calculate_surface_area(radius):
    """
    Calculate the surface area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The surface area of the circle.
    """
    return math.pi * (radius ** 2)