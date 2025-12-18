"""
QUESTION:
Create a function `find_triangle_area` to calculate the area of a triangle when given its base, height, and the lengths of its three sides. The function should use Heron's formula to calculate the area based on the side lengths, regardless of the given base and height. The input will be four arguments: the base, the height, and the lengths of the three sides.
"""

import math

def find_triangle_area(base, height, side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area