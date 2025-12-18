"""
QUESTION:
Compose a function `frustum_surface_area(r1, r2, h)` to compute the surface area of a conical frustum. The function should take three parameters: `r1` and `r2` as the radii of the two bases and `h` as the height of the frustum. The function should return the surface area using the formula `pi * (r1 + r2) * sqrt((r2 - r1)^2 + h^2) + pi * (r1^2 + r2^2)`.
"""

from math import pi, sqrt

def frustum_surface_area(r1, r2, h):
    return pi * (r1 + r2) * sqrt((r2 - r1)**2 + h**2) + pi * (r1**2 + r2**2)