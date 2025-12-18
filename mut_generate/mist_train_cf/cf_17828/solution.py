"""
QUESTION:
Implement a Python function `calculate_area` that calculates the area of a triangle given its three sides. The function should verify if the given sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If the sides do not form a valid triangle, the function should return an error message. The function should also implement a helper function `calculate_perimeter` to calculate the perimeter of the triangle using the given sides, rounded to two decimal places. The area should be calculated using Heron's formula and rounded to two decimal places.
"""

import math

def calculate_area(side1, side2, side3):
    # Check if the given sides form a valid triangle
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        # Calculate the semi-perimeter
        semi_perimeter = (side1 + side2 + side3) / 2
        
        # Calculate the area using Heron's formula
        area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
        
        # Round the area to two decimal places
        area = round(area, 2)
        
        return area
    else:
        return "Invalid triangle sides"

    # Round the perimeter to two decimal places
    def calculate_perimeter(side1, side2, side3):
        perimeter = round(side1 + side2 + side3, 2)
        return perimeter
    perimeter = calculate_perimeter(side1, side2, side3)
    return perimeter