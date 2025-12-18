"""
QUESTION:
Write a function named `get_triangle` that calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius, the coordinates of its vertices, and its perimeter. The semicircle is centered at the origin (0,0) and its radius is a positive floating-point number. The function should return a tuple containing the area of the triangle, the coordinates of its vertices, and its perimeter.
"""

import math

def get_triangle(radius):
    a = (-radius, 0)
    b = (radius, 0)
    c = (0, radius)

    area = ((2*radius)**2 * math.sqrt(3)) / 4
    perimeter = 3 * (2*radius)

    return area, a, b, c, perimeter