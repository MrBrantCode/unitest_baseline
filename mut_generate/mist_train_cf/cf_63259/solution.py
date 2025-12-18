"""
QUESTION:
Create a function named `calculate_circle` that calculates the circumference, area, and diameter of a circle given its radius, and another function named `calculate_sphere` that calculates the volume and surface area of a sphere given its radius. The program should be able to handle multiple calculations and changes in radii in an interactive mode, and it should also be able to calculate the change in properties when the radius changes. The program should be robust and efficient, validating inputs and preventing potential errors. The radius and change in radius should be input by the user.
"""

import math

def calculate_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    diameter = 2 * radius
    return circumference, area, diameter

def calculate_sphere(radius):
    volume = 4/3 * math.pi * radius ** 3
    surface_area = 4 * math.pi * radius ** 2
    return volume, surface_area