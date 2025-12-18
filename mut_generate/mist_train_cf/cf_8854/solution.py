"""
QUESTION:
Create a function `calculate_triangle_area` that calculates the area of a triangle given the lengths of its three sides. The function should take three parameters: `side1`, `side2`, and `side3`, which are the lengths of the sides of the triangle. The function should return the area of the triangle as a floating-point value. 

The function should validate that the lengths provided form a valid triangle, where the sum of any two sides is greater than the third side. If the lengths do not form a valid triangle, the function should raise an exception `InvalidTriangleException` with the message "Invalid triangle sides". Additionally, if the triangle is a degenerate triangle, where the sum of any two sides is equal to the third side, the function should raise an exception `DegenerateTriangleException` with the message "Degenerate triangle".

The function should handle floating-point values for the side lengths and use the mathematical formula for calculating the area of a triangle.
"""

import math

class InvalidTriangleException(Exception):
    pass

class DegenerateTriangleException(Exception):
    pass

def calculate_triangle_area(side1: float, side2: float, side3: float) -> float:
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        raise InvalidTriangleException("Invalid triangle sides")

    if (side1 + side2 == side3 or side1 + side3 == side2 or side2 + side3 == side1):
        raise DegenerateTriangleException("Degenerate triangle")

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area