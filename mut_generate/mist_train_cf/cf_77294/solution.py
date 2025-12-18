"""
QUESTION:
Calculate the area of a non-right triangle using Heron's formula given the side lengths and the proportions of the angle bisectors. 

Write a function named calculate_area that takes the side lengths of a triangle as input and returns the area of the triangle. The function should also be able to calculate the lengths of the angle bisectors and the inradius given the proportions of the angle bisectors. 

The function should assume that the input side lengths are valid and the proportions of the angle bisectors add up to 1.
"""

import math

def calculate_area(a, b, c):
    """
    Calculate the area of a non-right triangle using Heron's formula.

    Args:
    a (float): The length of side a.
    b (float): The length of side b.
    c (float): The length of side c.

    Returns:
    float: The area of the triangle.
    """
    s = (a + b + c) / 2 
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Calculate the lengths of the angle bisectors
    angle_bisector_ab = 2 * math.sqrt(a * b * (a + b - c) * (a + b + c)) / (a + b)
    angle_bisector_bc = 2 * math.sqrt(b * c * (b + c - a) * (b + c + a)) / (b + c)
    angle_bisector_ca = 2 * math.sqrt(c * a * (c + a - b) * (c + a + b)) / (c + a)

    # Calculate the inradius
    inradius = area / s

    return area, [angle_bisector_ab, angle_bisector_bc, angle_bisector_ca], inradius