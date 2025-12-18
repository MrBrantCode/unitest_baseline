"""
QUESTION:
Write a function `calculate_triangle_area` that takes three arguments `side1`, `side2`, and `side3` representing the lengths of the sides of a triangle. 

The function should first check if the given sides form a valid triangle by satisfying the triangle inequality theorem (the sum of any two sides must be greater than the third side). If the sides do not satisfy this condition, the function should return an error message. 

If the sides form a valid triangle, the function should calculate the area using Heron's formula, which involves the semi-perimeter `s = (side1 + side2 + side3) / 2`, and return the calculated area. The result should be a string in the format "Area of the triangle is {area}". 

Note that the function should handle the calculation of the square root, and the calculated area may be a decimal value.
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