"""
QUESTION:
Develop a function called `tetrahedron_surface_area` that calculates the surface area of a regular tetrahedron, given the lengths of its three edges a, b, and c. The function should return the calculated surface area. The tetrahedron is assumed to be regular, meaning all its edges are of equal length, although the function will still work for irregular tetrahedrons, the results may not be accurate.
"""

import math

def tetrahedron_surface_area(a, b, c):
    return math.sqrt(4*(a*a*b*b + a*a*c*c + b*b*c*c) - (a*a*a*a + b*b*b*b + c*c*c*c)) / 4