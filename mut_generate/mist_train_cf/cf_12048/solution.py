"""
QUESTION:
Create a function `calculate_triangle_perimeter` that takes three parameters: the lengths of all three sides of a triangle (`side1`, `side2`, `side3`). The function should validate the lengths according to the triangle inequality theorem (i.e., the sum of any two sides must be greater than the third side) and raise a custom exception with an error message if the lengths do not form a valid triangle. If the lengths are valid, the function should return the perimeter of the triangle.
"""

class InvalidTriangleException(Exception):
    pass

def calculate_triangle_perimeter(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise InvalidTriangleException("The lengths provided do not form a valid triangle.")
    else:
        perimeter = side1 + side2 + side3
        return perimeter