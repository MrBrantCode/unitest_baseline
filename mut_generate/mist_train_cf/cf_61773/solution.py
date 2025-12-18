"""
QUESTION:
Create a program with the following functions: `triangle_type(side1, side2, side3)`, `is_valid(side1, side2, side3)`, and `area(side1, side2, side3)`. The `triangle_type` function should return the type of triangle ("Equilateral", "Isosceles", or "Scalene") based on the given sides. The `is_valid` function should return `True` if the triangle is valid according to the triangle inequality theorem and `False` otherwise. The `area` function should calculate the area of the triangle using Heron's formula. The program should use these functions to determine the type and area of a triangle given the lengths of its sides, and print whether the triangle is valid or not.
"""

import math

def triangle_type(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

def is_valid(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False

def area(side1, side2, side3):
    # using Heron's formula
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))