"""
QUESTION:
Write a function `calculate_triangle_area` that takes three arguments representing the lengths of the sides of a triangle. The function should first check if the given sides form a valid triangle by satisfying the triangle inequality theorem, where the sum of any two sides must be greater than the third side. If the sides do not form a valid triangle, return an error message. Otherwise, calculate the area of the triangle using Heron's formula, which is `sqrt(s * (s - a) * (s - b) * (s - c))`, where `s` is the semi-perimeter `(a + b + c) / 2`. Return the calculated area rounded to two decimal places.
"""

import math

def calculate_triangle_area(side1, side2, side3):
    # Check if the given sides form a valid triangle
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Invalid triangle. The given sides do not satisfy the triangle inequality theorem."
    
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    # Return the calculated area
    return round(area, 2)