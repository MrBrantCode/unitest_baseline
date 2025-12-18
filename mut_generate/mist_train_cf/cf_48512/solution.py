"""
QUESTION:
Create a function `calculate_frustum_lateral_surface_area` that calculates the lateral surface area of a frustum given the radii of its two circular bases and its oblique height. The function should take three parameters: `r1` and `r2` for the radii, and `s` for the oblique height. The function should return an error message if any of the input parameters are negative.
"""

import math

def calculate_frustum_lateral_surface_area(r1, r2, s):
    if r1 < 0 or r2 < 0 or s < 0:
        return "Error: the radii and height must be positive numbers."

    lateral_surface_area = math.pi * (r1 + r2) * math.sqrt((r1 - r2)**2 + s**2)

    return lateral_surface_area