"""
QUESTION:
Create a function `circle_properties` that takes the radius of a circle as input and returns the area and circumference of the circle. Use the formulas for the area (A = πr^2) and circumference (C = 2πr) of a circle in your calculation. The function should return two values: the area and the circumference of the circle.
"""

import math

def circle_properties(radius):
    # Calculate the area of the circle
    area = math.pi * radius**2
    
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius
    
    return area, circumference