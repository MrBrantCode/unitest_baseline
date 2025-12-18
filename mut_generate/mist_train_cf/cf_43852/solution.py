"""
QUESTION:
Create a function named `get_triangle` that takes one parameter `radius`. The function should calculate and return the area and perimeter of an equilateral triangle inscribed in a semicircle, along with the coordinates of its vertices. The side length of the triangle is equal to the diameter of the semicircle, which is twice the radius.
"""

import math

def get_triangle(radius):
    a = (-radius, 0)
    b = (radius, 0)
    c = (0, radius)
    area = ((2*radius)**2 * math.sqrt(3)) / 4
    perimeter = 3 * (2*radius)
    return area, a, b, c, perimeter