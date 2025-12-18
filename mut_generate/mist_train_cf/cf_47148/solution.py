"""
QUESTION:
Write a function `calculate_tetrahedron` that takes the side length of a regular tetrahedron as input and returns its surface area and volume, both rounded to 2 decimal places.
"""

import math

def calculate_tetrahedron(side):
    # Calculate surface area
    surface_area = round(math.sqrt(3) * side ** 2, 2)

    # Calculate volume
    volume = round((side ** 3) / (6 * math.sqrt(2)), 2)

    return surface_area, volume