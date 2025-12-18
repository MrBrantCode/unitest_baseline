"""
QUESTION:
Create a function `compute_pentagon_properties` that takes in the parameters of a triangle and a rectangle within an irregular pentagon: the side opposite a known angle `a`, another side of the triangle `b`, the angle `alpha` in degrees, and the length `l` and width `w` of the rectangle. The function should return the altitude and area of the pentagon. The pentagon is constructed from the triangle and rectangle in a specific arrangement where the rectangle is 'on top' of the triangle. Note that the angle `alpha` should be converted from degrees to radians before applying it.
"""

import math

def compute_pentagon_properties(a, b, alpha, l, w):
    # convert angle in degrees to radians
    alpha = math.radians(alpha)
    
    # compute properties of the triangle
    h_triangle = b * math.sin(alpha)
    area_triangle = 0.5 * a * h_triangle
    
    # compute properties of the rectangle
    area_rectangle = l * w
    h_rectangle = w
    
    # compose the pentagon properties
    h_pentagon = h_triangle + h_rectangle
    area_pentagon = area_triangle + area_rectangle
    
    return h_pentagon, area_pentagon