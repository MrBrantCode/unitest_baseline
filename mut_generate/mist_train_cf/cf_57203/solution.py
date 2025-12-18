"""
QUESTION:
Create a function named `calculate_circle_area(radius)` that calculates the area of a circle given its radius using the formula A = πr². The function should accept a single numeric argument `radius` and return the calculated area. If the input is non-numeric or negative, the function should return an error message.
"""

import math

def calculate_circle_area(radius):
    if isinstance(radius, (int, float)):
        if radius > 0:
            return math.pi * radius * radius
        else:
            return "Error: Radius should be positive."
    else:
        return "Error: Non-numeric input."