"""
QUESTION:
Calculate the total exterior surface area of a hemiellipsoidal dome using the function `calculate_hemiellipsoid_surface_area`. The function should take in three parameters: `a`, `b`, and `c`, representing the semi-principal axes of the ellipsoid. The function should return the surface area of the hemiellipsoid, considering surface texture properties like roughness and depressions as a factor `k` that will be multiplied with the calculated surface area.
"""

import math

def calculate_hemiellipsoid_surface_area(a, b, c, k):
    """
    Calculate the total exterior surface area of a hemiellipsoidal dome.

    Parameters:
    a (float): Semi-principal axis a of the ellipsoid.
    b (float): Semi-principal axis b of the ellipsoid.
    c (float): Semi-principal axis c of the ellipsoid.
    k (float): Factor accounting for surface texture properties like roughness and depressions.

    Returns:
    float: The surface area of the hemiellipsoid.
    """
    surface_area = 2 * math.pi * (((a**(2/3)*b**(2/3) + a**(2/3)*c**(2/3) + b**(2/3)*c**(2/3))/3)**(3/2))
    return k * surface_area