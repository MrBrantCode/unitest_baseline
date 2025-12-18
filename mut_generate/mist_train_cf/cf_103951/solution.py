"""
QUESTION:
Create a function `calculate_circle_area(radius)` that calculates the area of a circle given a positive integer radius. If the input radius is 0 or negative, the function should return an error message.
"""

import math

def calculate_circle_area(radius):
    if radius <= 0:
        return "Error: Radius must be a positive integer."
    else:
        area = math.pi * radius**2
        return area