"""
QUESTION:
Create a Python function named `calculate_circle_properties` that takes the radius of a circle as input and returns the area and circumference of the circle. The formulas for area and circumference are A = πr^2 and C = 2πr, respectively.
"""

import math

def calculate_circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference