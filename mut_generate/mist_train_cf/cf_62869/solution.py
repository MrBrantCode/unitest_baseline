"""
QUESTION:
Create a function named `frustum_surface_area` that takes three parameters: the radii of the two circular bases (`r1` and `r2`) and the slant height (`h_slant`), and returns the surface area of a frustum using the formula `π(r1 + r2) * h_slant + π(r1^2 + r2^2)`.
"""

import math

def frustum_surface_area(r1, r2, h_slant):
    return math.pi * (r1 + r2) * h_slant + math.pi * (r1**2 + r2**2)