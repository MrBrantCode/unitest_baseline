"""
QUESTION:
Given a semicircle centered at the origin with a radius, develop a function `triangle_properties` that calculates the properties of the inscribed triangle with the maximum possible area. The function should return a dictionary containing the vertices' coordinates, the triangle's area, perimeter, inradius, and circumradius. Assume the radius is a positive floating point number.
"""

import math

def triangle_properties(radius):
    #vertices of triangle
    v1 = (0, 0)
    v2 = (-radius, 0)
    v3 = (0, radius)
    
    #triangle properties
    area = (radius * radius) / 2
    perimeter = 2 * radius + math.sqrt(2) * radius
    
    #inradius and circumradius
    inradius = radius * (1 - 1/math.sqrt(2))
    circumradius = radius/2 * math.sqrt(2)
    
    return {'Vertices': (v1,v2,v3), 
            'Area': area, 
            'Perimeter': perimeter, 
            'Inradius': inradius, 
            'Circumradius': circumradius}