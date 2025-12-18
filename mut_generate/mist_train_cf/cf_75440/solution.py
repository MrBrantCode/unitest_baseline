"""
QUESTION:
Write a function named `sphere_surface_area` that calculates the surface area of a sphere given its radius. The surface area of a sphere is calculated using the formula 4 * π * r^2. Implement this function in a way that takes a radius as input and returns the calculated surface area.
"""

import math

def sphere_surface_area(radius):
    return 4 * math.pi * (radius ** 2)