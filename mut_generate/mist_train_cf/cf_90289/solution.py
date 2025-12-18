"""
QUESTION:
Write a function named `calculate_triangle_area` that takes three arguments `side1`, `side2`, and `side3` representing the lengths of the sides of a triangle. The function should first check if the given sides form a valid triangle by satisfying the triangle inequality theorem. If the sides do not satisfy this condition, return an error message. If the sides form a valid triangle, calculate the area using Heron's formula and return the result rounded to two decimal places.
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