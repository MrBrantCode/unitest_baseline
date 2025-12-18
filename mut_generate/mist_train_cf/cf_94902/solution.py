"""
QUESTION:
Implement a function `calculate_area` that calculates the area of a triangle given its three sides and returns the result rounded to two decimal places. The function should also verify if the given sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If the sides do not form a valid triangle, the function should return an error message.

Additionally, implement a function `calculate_perimeter` that calculates the perimeter of the triangle using the given sides and returns the result rounded to two decimal places.

The `calculate_area` function should use Heron's formula to calculate the area. The semi-perimeter, which is half of the perimeter, should be used in the calculation.
"""

import math

def calculate_area(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        perimeter = side1 + side2 + side3
        semi_perimeter = perimeter / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
        area = round(area, 2)
        return area
    else:
        return "Invalid triangle sides"

def calculate_perimeter(side1, side2, side3):
    perimeter = side1 + side2 + side3
    perimeter = round(perimeter, 2)
    return perimeter