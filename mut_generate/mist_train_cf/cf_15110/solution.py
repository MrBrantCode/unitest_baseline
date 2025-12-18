"""
QUESTION:
Create a function called `calculate_circle_area` that takes a string input representing the radius of a circle. The function should calculate and return the area of the circle using the formula πr², where r is the radius. If the input string cannot be converted to a valid positive number, the function should return an error message.
"""

import math

def calculate_circle_area(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            return "Error: Radius must be a positive number."
        else:
            area = math.pi * (radius ** 2)
            return area
    except ValueError:
        return "Error: Invalid input. Radius must be a valid number."