"""
QUESTION:
Define a function named `calculate_triangle_perimeter` that takes three parameters `side1`, `side2`, and `side3` representing the lengths of the sides of a triangle. The function should calculate the perimeter of the triangle if the provided lengths form a valid triangle according to the triangle inequality theorem (i.e., the sum of the lengths of any two sides must be greater than the length of the third side). If the lengths do not form a valid triangle, the function should raise a custom exception with an error message.
"""

class InvalidTriangleException(Exception):
    pass

def calculate_triangle_perimeter(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise InvalidTriangleException("The lengths provided do not form a valid triangle.")
    else:
        perimeter = side1 + side2 + side3
        return perimeter