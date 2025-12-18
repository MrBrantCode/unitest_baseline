"""
QUESTION:
Create a function named `calculate_area` that takes three arguments `side1`, `side2`, and `side3` representing the sides of a triangle. The function should return the area of the triangle rounded to two decimal places if the given sides form a valid triangle, where the sum of any two sides is greater than the third side. If the sides do not form a valid triangle, return "Error: Invalid triangle sides".
"""

import math

def calculate_area(side1, side2, side3):
    # Check if the sides form a valid triangle
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        # Calculate the semi-perimeter
        s = (side1 + side2 + side3) / 2

        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

        # Round the calculated area to two decimal places
        area = round(area, 2)

        return area
    else:
        return "Error: Invalid triangle sides"