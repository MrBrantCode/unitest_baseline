"""
QUESTION:
Write a function `calculate_sector_area(radius, angle)` that calculates the area of a sector of a circle given the radius and central angle in degrees. The function should return the area as a floating point number. Use the math library for the value of PI.
"""

import math

def calculate_sector_area(radius, angle):
    return (angle / 360) * math.pi * radius ** 2