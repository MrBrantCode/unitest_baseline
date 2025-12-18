"""
QUESTION:
Write a function named `calculate_triangle_area` that takes three arguments, `side1`, `side2`, and `side3`, representing the lengths of the sides of a triangle. The function should return the area of the triangle if the given sides form a valid triangle, and an error message otherwise. A valid triangle should satisfy the triangle inequality theorem, where the sum of any two sides is greater than the third side. If the triangle is valid, use Heron's formula to calculate the area.
"""

import math

def calculate_triangle_area(side1, side2, side3):
    # Check if the sides form a valid triangle
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Error: Invalid triangle. The sum of any two sides should be greater than the third side."
    
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    return area