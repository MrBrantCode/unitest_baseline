"""
QUESTION:
Write a function `compute_triangle_area(a, b, c)` that calculates the area of a triangle given the lengths of its sides `a`, `b`, and `c`, where the angle between sides `a` and `b` is unknown but the lengths satisfy the triangle inequality (i.e., the sum of the lengths of any two sides is greater than the length of the third side). The function should use the Law of Cosines to calculate the angle between sides `a` and `b` and then use this angle to compute the area of the triangle. The angle should be handled in radians.
"""

import math

def compute_triangle_area(a, b, c):
    cos_theta = (a**2 + b**2 - c**2) / (2*a*b)
    theta = math.acos(cos_theta)
    area = 0.5 * a * b * math.sin(theta)
    return area