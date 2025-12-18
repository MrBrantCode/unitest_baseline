"""
QUESTION:
Write a function `calculate_circle_surface_area` that calculates the surface area of a circle given its radius. Use the mathematical formula A = πr², where A is the surface area and r is the radius. The function should take one argument: `radius`. The function should return the calculated surface area.
"""

import math

def calculate_circle_surface_area(radius):
    """
    Calculate the surface area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The surface area of the circle.
    """
    return math.pi * (radius**2)