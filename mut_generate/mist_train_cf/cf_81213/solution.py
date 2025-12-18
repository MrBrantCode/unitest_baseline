"""
QUESTION:
Develop a function named `largest_triangle` that calculates the area of the largest triangle that can be inscribed within a semicircle of a given radius and returns the area along with the coordinates of the triangle's vertices. The function should take one argument, the radius of the semicircle, and return an error message if the input radius is not a positive number.
"""

import math

def largest_triangle(radius):
    # Ensure radius is a positive number.
    if radius <= 0:
        return 'Error: Radius must be a positive number.'

    # Calculate area using formula for area of triangle: 1/2 * base * height.
    # For the largest triangle in a semicircle, base = height = radius.
    area = 0.5 * radius ** 2
    return area, [(-radius, 0), (radius, 0), (0, radius)]