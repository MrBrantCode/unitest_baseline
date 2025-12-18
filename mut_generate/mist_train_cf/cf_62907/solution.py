"""
QUESTION:
Create a function named `triangle_properties(a, b, c)` that calculates the area, type (equilateral, isosceles, scalene), interior angles, and circumradius of a triangle given the lengths of its three sides `a`, `b`, and `c`. The function should validate whether the sides can form a valid triangle, where the sum of each pair of sides exceeds the length of the remaining side. If the sides do not form a valid triangle, the function should return -1. Otherwise, the function should return a tuple containing the area rounded to 2 decimal points, the type of the triangle, a tuple of the three interior angles rounded to 2 decimal points, and the circumradius rounded to 2 decimal points.
"""

import math

def triangle_properties(a, b, c):
    # check if sides can form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # find the type of the triangle
    if a == b == c:
        triangle_type = 'Equilateral'
    elif a == b or a == c or b == c:
        triangle_type = 'Isosceles'
    else:
        triangle_type = 'Scalene'

    # compute the semi-perimeter
    s = (a + b + c) / 2
    # calculate the area
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # find the circumradius
    circumradius = (a * b * c) / (4 * area)
    
    # calculate the three angles using the law of cosines
    cos_a = (b**2 + c**2 - a**2) / (2 * b * c)
    angle_a = math.degrees(math.acos(cos_a))
    
    cos_b = (c**2 + a**2 - b**2) / (2 * c * a)
    angle_b = math.degrees(math.acos(cos_b))
    
    cos_c = (a**2 + b**2 - c**2) / (2 * a * b)
    angle_c = math.degrees(math.acos(cos_c))
    
    # round to 2 decimal points
    area = round(area, 2)
    circumradius = round(circumradius, 2)
    angle_a = round(angle_a, 2)
    angle_b = round(angle_b, 2)
    angle_c = round(angle_c, 2)

    return (area, triangle_type, (angle_a, angle_b, angle_c), circumradius)