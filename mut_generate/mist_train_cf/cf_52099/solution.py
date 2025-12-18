"""
QUESTION:
Write a function named `calculate_area` that takes three parameters: `side1`, `side2`, and `base`, representing the sides of an isosceles triangle with unequal bases but equal sides. 

The function should first check if all sides are greater than 0 and if the sum of the lengths of any two sides is greater than the length of the third side (triangle inequality theorem). If either condition is not met, return an error message.

If the input is valid, use the semi-perimeter method to calculate and return the area of the triangle.
"""

import math

def calculate_area(side1, side2, base):
    # Error checking
    if side1 <= 0 or side2 <= 0 or base <= 0:
        return "Error: All sides must be greater than 0"
    if not (side1 + side2 > base and side1 + base > side2 and side2 + base > side1):
        return "Error: The triangle inequality theorem is violated"

    # Calculation
    semi_perimeter = (side1 + side2 + base) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - base))
    return area