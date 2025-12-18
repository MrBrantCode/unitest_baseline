"""
QUESTION:
Write a function named `equilateral_triangle_area` that calculates the area of an equilateral triangle given the length of its side. The function should use the formula for the area of an equilateral triangle: `(side^2 * sqrt(3)) / 4`.
"""

import math

def equilateral_triangle_area(side):
    area = (side ** 2) * math.sqrt(3) / 4
    return area