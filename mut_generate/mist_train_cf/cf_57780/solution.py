"""
QUESTION:
Compute and return the area and the altitude of a triangle from its three side lengths. The triangle should be either an isosceles (two sides are equal) or a scalene triangle (all sides have unequal lengths). The function should return area and altitude with a precision of 2 decimal points. If the sides cannot form a valid triangle or the triangle is equilateral (all sides are equal), return -1. A triangle is valid if the sum of any two sides is greater than the length of the third side.
"""

import math

def entrance(a, b, c):
    """Compute and return the area and the altitude of a triangle from its three side lengths"""
    
    # check if the sides can form a valid triangle
    if a + b <= c or b + c <= a or a + c <= b:
        return -1
    
    # check if the triangle is equilateral
    if a == b == c:
        return -1

    # calculate semi-perimeter
    s = (a + b + c) / 2

    # calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = round(area, 2)

    # calculate altitude
    # altitude = 2 * area / base
    # assume c is the base for computing the altitude.
    # for isosceles triangle, any side can be considered as base.
    # for scalene triangle, the altitude varies with the chosen base.
    altitude = 2 * area / c
    altitude = round(altitude, 2)

    return (area, altitude)