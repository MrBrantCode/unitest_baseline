"""
QUESTION:
Write a function `calculate_circle` that calculates the area and circumference of a circle given its radius. The radius must be a positive non-zero number. The function should return the area and circumference rounded to the nearest integer.
"""

import math

def calculate_circle(radius):
    if radius <= 0:
        return "Radius must be a positive non-zero number."
    
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    
    return "Area: " + str(round(area)) + "\nCircumference: " + str(round(circumference))