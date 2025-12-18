"""
QUESTION:
Write a Python function `inscribed_triangle_properties` to calculate the properties of the largest triangle that can be inscribed in a semicircle with a given radius. The semicircle is centered at the origin (0,0) and the radius is a positive floating point number. The function should return the area of the triangle, the coordinates of the vertices, the perimeter of the triangle, the length of the inradius, and the length of the circumradius.
"""

import math

def inscribed_triangle_properties(radius):
    # calculate the area
    area = math.sqrt(4*radius*radius - radius*radius)
    # coordinates of vertices
    vertices = [(0, radius), (-radius, -radius), (radius, -radius)]
    # calculate the perimeter
    perimeter = 2 * radius * (math.sqrt(2) + 1)
    # calculate inradius and circumradius
    inradius = radius/math.sqrt(2)
    circumradius = radius

    return area, vertices, perimeter, inradius, circumradius