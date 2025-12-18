"""
QUESTION:
Write a function `square_area_from_circumference` that calculates the area of a square, given that the length of each side of the square equals the radius of a circle with a known circumference. The circumference is the input to the function.
"""

import math

def square_area_from_circumference(circumference):
    radius = circumference / (2 * math.pi)
    return radius ** 2