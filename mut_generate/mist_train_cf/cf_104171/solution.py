"""
QUESTION:
Define a function called `triangle_type` that takes three integer arguments representing the lengths of the sides of a triangle. The function should check the validity of the triangle and return the type of the triangle. The triangle is valid if all sides are positive and the sum of any two sides is greater than the third side. If the triangle is valid, the function should return the type of the triangle: "Equilateral triangle" if all sides are equal, "Isosceles triangle" if exactly two sides are equal, and "Scalene triangle" if no sides are equal. If the triangle is invalid, the function should print an error message and return.
"""

def triangle_type(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Error: Sides cannot be zero or negative.")
        return
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("Error: Invalid triangle.")
        return
    if side1 == side2 == side3:
        return "Equilateral triangle"
    if side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles triangle"
    return "Scalene triangle"