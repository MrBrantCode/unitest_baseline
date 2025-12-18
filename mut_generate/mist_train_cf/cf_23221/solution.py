"""
QUESTION:
Write a function called `calculate_triangle_area` that takes three parameters `side1`, `side2`, and `side3` representing the lengths of three sides of a triangle. The function should return the area of the triangle and raise a custom `InvalidTriangleException` if the lengths do not form a valid triangle (i.e., the sum of any two sides is not greater than the third side).
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