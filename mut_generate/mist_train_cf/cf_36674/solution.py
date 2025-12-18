"""
QUESTION:
Create a function called `calculate_polygon_area` that takes two parameters: `n` (an integer representing the number of sides of a regular polygon) and `s` (a float representing the length of each side of the regular polygon). Calculate the area of the regular polygon using the formula `Area = (n * s^2) / (4 * tan(π/n))` and return the result.
"""

import math

def calculate_polygon_area(n, s):
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area