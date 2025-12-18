"""
QUESTION:
Implement a function `calculate_polygon_area(n, s)` that calculates the area of a regular polygon. The function should take two parameters: the number of sides `n`, an integer greater than 2, and the length of each side `s`, a positive float. The function should return the calculated area.
"""

import math

def calculate_polygon_area(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))