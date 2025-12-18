"""
QUESTION:
Create a function `calculate_area(side1, side2, side3)` that calculates the area of a triangle given its three sides. The function should first check if the sides form a valid triangle by verifying if the sum of any two sides is greater than the third side. If the sides form a valid triangle, it should calculate the area using Heron's formula and round the result to two decimal places. If the sides do not form a valid triangle, it should return an error message.
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