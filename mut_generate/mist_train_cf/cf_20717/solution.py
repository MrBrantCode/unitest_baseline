"""
QUESTION:
Write a function to calculate the area and perimeter of a triangle given the lengths of its three sides. The function should check if the entered values form a valid triangle and handle invalid inputs. It should also determine whether the triangle is right-angled. The function should repeat the calculation until the user chooses to exit.

The area of the triangle should be calculated using Heron's formula: Area = √(s * (s - side1) * (s - side2) * (s - side3)), where s = (side1 + side2 + side3) / 2.

Assume the input values are non-negative numbers and the user will enter either 'yes' or 'no' to continue or exit the program.
"""

import math

def calculate_triangle_properties(side1, side2, side3):
    """
    Calculate the area, perimeter, and check if a triangle is right-angled given its three sides.

    Args:
        side1 (float): The length of side 1.
        side2 (float): The length of side 2.
        side3 (float): The length of side 3.

    Returns:
        tuple: A tuple containing a boolean indicating if the triangle is valid, its area, its perimeter, and a boolean indicating if it's right-angled.
    """

    # Check if the sides form a valid triangle
    is_valid = side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2

    if not is_valid:
        return False, None, None, False

    # Calculate the area using Heron's formula
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Check if the triangle is right-angled
    sides = [side1, side2, side3]
    sides.sort()
    is_right_angled = sides[2]**2 == sides[0]**2 + sides[1]**2

    return True, area, perimeter, is_right_angled