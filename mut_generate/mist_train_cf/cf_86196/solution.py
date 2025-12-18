"""
QUESTION:
Create a function named `calculate_circle_area` that takes a string representing the radius of a circle as input and returns the calculated area as a string with exactly two decimal places. The function should validate that the input can be converted to a positive number and return an error message if the input is not a valid number or if the radius is not positive.
"""

import math

def calculate_circle_area(radius):
    try:
        radius = float(radius)
        if radius <= 0:
            return "Error: Radius must be a positive number"
        area = math.pi * radius**2
        return "{:.2f}".format(area)
    except ValueError:
        return "Error: Invalid input. Radius must be a number"