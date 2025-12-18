"""
QUESTION:
Create a function named `calculate_circle_area` that calculates the area of a circle given its radius. The radius should be a positive integer greater than 0 and less than or equal to 10^9. The function should return an error message for invalid radii, specifically when the radius is less than or equal to 0 or greater than 10^9.
"""

import math

def calculate_circle_area(radius):
    if radius <= 0:
        return "Error: Radius must be a positive integer greater than 0."
    elif radius > 10**9:
        return "Error: Radius is too large."
    else:
        return math.pi * radius**2