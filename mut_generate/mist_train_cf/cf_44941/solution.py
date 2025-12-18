"""
QUESTION:
Write a function `max_triangle_semicircle(h, k, r)` to find the area of the largest triangle that can be inscribed in a semicircle with radius `r` centered at point `(h, k)` in the 2D plane. The function should also determine the coordinates of the vertices of this triangle. The radius `r` is a positive integer, and `h` and `k` can be any integer (positive or negative). The function should return the area of the triangle and the coordinates of the vertices.
"""

import math

def max_triangle_semicircle(h=0, k=0, r=1):
    if r <= 0:
        return None, None
        
    area = r**2
    vertices = [(h-r, k), (h+r, k), (h, k+r)]
    return area, vertices