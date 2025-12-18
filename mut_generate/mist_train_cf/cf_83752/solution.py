"""
QUESTION:
Create a function `surface_area_dome(a, b, c)` that calculates the total exterior surface area of a hemiellipsoidal dome with semi-axes of lengths `a`, `b`, and `c`. Use the formula `A_dome = 2π[(a^1.6b^1.6 + a^1.6c^1.6 + b^1.6c^1.6)/3]^0.625` to calculate the surface area. Note that this approximation may not be completely accurate when the three axes are very different in size.
"""

import math

def surface_area_dome(a, b, c):
    """Function to calculate surface area of a hemi-ellipsoid dome."""
    
    return 2 * math.pi * pow((pow(a, 1.6) * pow(b, 1.6)
                           + pow(a, 1.6) * pow(c, 1.6)
                           + pow(b, 1.6) * pow(c, 1.6)) / 3, 0.625)