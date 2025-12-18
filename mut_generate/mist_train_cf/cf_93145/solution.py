"""
QUESTION:
Create a function named `calculate_triangle_area` that takes three arguments representing the lengths of the sides of a triangle (a, b, c) and returns the area of the triangle rounded to the nearest whole number. If the triangle is invalid (i.e., the sum of any two sides is less than or equal to the third side), the function should return "Invalid triangle".
"""

import math

def calculate_triangle_area(a, b, c):
    # Check if the triangle is valid
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        return "Invalid triangle"
    
    # Calculate the semiperimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Round the area to the nearest whole number
    return round(area)