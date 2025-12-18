"""
QUESTION:
Create a function called `calculate_triangle_area` that takes three positive integer parameters: `side1`, `side2`, and `side3`, representing the lengths of the three sides of a triangle. The function should return the area of the triangle if it is valid (i.e., the sum of any two sides is greater than the third side), and 0 otherwise. Use Heron's formula to calculate the area and round it to the nearest whole number. The time complexity should not exceed O(n^2) and the space complexity should not exceed O(1).
"""

import math

def calculate_triangle_area(side1, side2, side3):
    # Check if the triangle is valid
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return 0
    
    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    
    # Round the area to the nearest whole number
    return round(area)