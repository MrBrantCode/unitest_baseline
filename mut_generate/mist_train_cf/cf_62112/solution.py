"""
QUESTION:
Create a function named `calculate_area` that accepts a list of tuples as parameters, where each tuple represents the lengths of two adjacent sides and the angle between these sides of a parallelogram. The function should return a list of areas of all the parallelograms using the formula: Area = side1 * side2 * sin(angle), considering that the angle is given in degrees and the math library's sin function takes the angle in radians.
"""

import math

def calculate_area(parallelograms):
    areas = []
    for p in parallelograms:
        angle_in_radians = math.radians(p[2])
        area = p[0] * p[1] * math.sin(angle_in_radians)
        areas.append(area)
    return areas