"""
QUESTION:
Write a function `is_valid_triangle(point1, point2, point3)` and `calc_triangle_area(point1, point2, point3)` that takes as input three points in a 3D space represented as lists of three numbers each. The function `is_valid_triangle(point1, point2, point3)` should return a boolean indicating whether the points can form a valid triangle, i.e., they are distinct and do not lie on a straight line. If `is_valid_triangle(point1, point2, point3)` returns True, then `calc_triangle_area(point1, point2, point3)` should return the area of the triangle using Heron's formula.
"""

import math

def is_valid_triangle(point1, point2, point3):
    """
    Check if three points in 3D space can form a valid triangle
    """
    # Check if all points are distinct
    if point1 == point2 or point1 == point3 or point2 == point3:
        return False

    # Check if all points lie on a straight line
    vector1 = [point2[i] - point1[i] for i in range(3)]
    vector2 = [point3[i] - point1[i] for i in range(3)]
    cross_product = [vector1[(i+1)%3]*vector2[(i+2)%3] - vector1[(i+2)%3]*vector2[(i+1)%3] for i in range(3)]
    if all(c == 0 for c in cross_product):
        return False

    return True

def calc_triangle_area(point1, point2, point3):
    """
    Calculate the area of a triangle in 3D space using Heron's formula
    """
    # Calculate the sides' lengths
    side1 = math.sqrt(sum((point2[i] - point1[i])**2 for i in range(3)))
    side2 = math.sqrt(sum((point3[i] - point2[i])**2 for i in range(3)))
    side3 = math.sqrt(sum((point1[i] - point3[i])**2 for i in range(3)))

    # Calculate the semi-perimeter
    s = 0.5 * (side1 + side2 + side3)

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area