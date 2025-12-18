"""
QUESTION:
Write a function `calculate_triangle_area(side1, side2, side3)` that calculates the area of a triangle given the lengths of its sides. The function should validate that the lengths form a valid triangle (i.e., the sum of any two sides is greater than the third side) and raise an `InvalidTriangleException` with an error message if the lengths are invalid.
"""

class InvalidTriangleException(Exception):
    pass

def calculate_triangle_area(side1, side2, side3):
    # Check if the lengths form a valid triangle
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise InvalidTriangleException("Invalid triangle: The sum of any two sides should be greater than the third side.")

    # Calculate the semi-perimeter of the triangle
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

    return area