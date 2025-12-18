"""
QUESTION:
Write a function named `frustum_surface_area` that takes three parameters: the radii of the two bases (`r1` and `r2`) and the slant height (`l`) of a frustum of a cone. The function should calculate and return the surface area of the frustum using the formula A = π(r1 + r2) * l + π*r1^2 + π*r2^2. Assume inputs are positive real numbers and do not include input error checking.
"""

import math

def frustum_surface_area(r1, r2, l):
    return math.pi*(r1 + r2)*l + math.pi*r1**2 + math.pi*r2**2