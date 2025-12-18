"""
QUESTION:
Write a function `calculate_triangle_perimeter` that takes three arguments representing the side lengths of a triangle. The function should calculate the perimeter of the triangle if the side lengths form a valid triangle (the sum of any two side lengths is greater than the third side length, and all side lengths are greater than 0) and return the type of the triangle ("equilateral", "isosceles", or "scalene") along with its perimeter. If the side lengths do not form a valid triangle, the function should return -1.
"""

def calculate_triangle_perimeter(side1, side2, side3):
    # Check if side lengths are valid
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return -1
    if (side1 + side2) <= side3 or (side2 + side3) <= side1 or (side1 + side3) <= side2:
        return -1

    # Calculate perimeter
    perimeter = side1 + side2 + side3

    # Check triangle type
    if side1 == side2 and side2 == side3:
        triangle_type = "equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    return triangle_type, perimeter