"""
QUESTION:
Implement the function `calculate_triangle_height(angle, side1, side2)` to calculate the height of a triangle given an angle in degrees and the lengths of the two sides that enclose the angle. The function should return the height of the triangle if the inputs form a valid triangle, otherwise return None. Ensure the angle is within the range (0, 180] and the sides are positive real numbers. Additionally, apply the triangle inequality principle to verify the inputs can form a valid triangle.
"""

import math

def calculate_triangle_height(angle, side1, side2):
    if angle <= 0 or angle >= 180:
        return None
    elif side1 <= 0 or side2 <= 0:
        return None
    elif side1 + side2 <= side1 or side1 + side2 <= side2 or side1 + side1 <= side2:
        return None
    else:
        height = side2 * math.sin(math.radians(angle))
        return height