"""
QUESTION:
Create a function `validate_input()` that checks if three given side lengths form a valid triangle and returns an error message if they do not. The function should check if the side lengths are valid numbers greater than zero and if they satisfy the triangle inequality theorem (i.e., the sum of any two sides of a triangle must be greater than the third side). If the side lengths are valid, the function should return an empty string.
"""

def validate_input(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid side lengths. Sides must be greater than zero."
    elif not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)) or not isinstance(side3, (int, float)):
        return "Invalid side lengths. Sides must be numbers."
    elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Invalid triangle. The sum of any two sides of a triangle must be greater than the third side."
    return ""