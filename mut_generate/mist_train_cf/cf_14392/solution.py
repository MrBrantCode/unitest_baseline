"""
QUESTION:
Write a function named find_circle_area that calculates the area of a circle given its diameter as input, using the formula A = π * (d/2)^2, where A is the area and d is the diameter.
"""

import math

def find_circle_area(diameter):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area