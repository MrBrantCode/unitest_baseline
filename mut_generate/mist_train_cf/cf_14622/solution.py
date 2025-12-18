"""
QUESTION:
Write a function named `calculate_triangle_area` that takes three parameters: `side1`, `side2`, and `side3`, representing the lengths of the sides of a triangle. The function should return the area of the triangle using Heron's formula, but first, it should check if the given sides form a valid triangle according to the triangle inequality theorem. If the sides do not form a valid triangle, the function should return an error message.
"""

import math

def calculate_triangle_area(side1, side2, side3):
    # Check if the sides form a valid triangle
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return "Error: Invalid triangle sides"
    
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    return "Area of the triangle is {}".format(area)