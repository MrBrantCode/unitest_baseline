"""
QUESTION:
Create a function named `calculate_area` that takes two arguments, `side_a` and `side_b`, representing the lengths of two sides of a right triangle. The function should use basic arithmetic operations to calculate the area of the triangle and handle the following cases: 
- Return an error message if either `side_a` or `side_b` is zero or negative.
- Return an error message if the triangle is not a right triangle, as verified using the Pythagorean theorem.
- The function should not use any built-in math functions or libraries.
"""

def calculate_area(side_a, side_b):
    # check if side_a or side_b are negative or zero
    if side_a <= 0 or side_b <= 0:
        return "Error: Sides must be positive numbers."

    # check if the triangle is a right triangle using Pythagorean theorem
    hypotenuse = (side_a ** 2 + side_b ** 2) ** 0.5
    if hypotenuse != max(side_a, side_b):
        return "Error: Not a right triangle."

    # calculate the area using basic arithmetic operations
    area = (side_a * side_b) / 2
    return area