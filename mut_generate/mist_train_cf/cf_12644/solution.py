"""
QUESTION:
Write a function `calculate_circle_properties(radius)` that takes the radius of a circle as input and returns its area and circumference. Use the mathematical constant pi (π) for the calculation, where the area is πr² and the circumference is 2πr. The function should return the calculated area and circumference as a tuple.
"""

import math

def calculate_circle_properties(radius):
    # Calculate area of the circle
    area = math.pi * radius**2

    # Calculate circumference of the circle
    circumference = 2 * math.pi * radius

    return area, circumference