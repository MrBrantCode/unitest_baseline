"""
QUESTION:
Write a Python function `max_triangle_semicircle(r)` that calculates the area of the largest triangle that can be inscribed in a semicircle with a given radius `r`, where `r` is a positive integer and the semicircle is centered at the origin (0,0). The function should also determine the coordinates of the vertices of this triangle. The function should return the area of the triangle and the coordinates of the vertices.
"""

import math

def max_triangle_semicircle(r):
    vertices = [(-r, 0), (r, 0), (0, r)]
    area = 0.5 * (2*r) * r
    return area, vertices