"""
QUESTION:
Create a function named `calculate_triangle_area` that takes three parameters representing the lengths of the sides of a triangle. The function should first check if the given sides form a valid triangle by satisfying the triangle inequality theorem (the sum of any two sides must be greater than the third side). If the sides are valid, calculate the area of the triangle using Heron's formula and return the result; otherwise, return an error message indicating that the sides do not form a valid triangle.
"""

import math

def calculate_triangle_area(a, b, c):
    # Check if the sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Error: Invalid triangle. The sum of any two sides should be greater than the third side."
    
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area