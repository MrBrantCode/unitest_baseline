"""
QUESTION:
Create a function `calculate_angle` that takes in three arguments representing the side lengths of a triangle. Using the Law of Cosines, calculate the angle in degrees opposite the third side. If the triangle is invalid (i.e., the sum of any two sides is less than or equal to the third side), return an error message instead.
"""

import math

def calculate_angle(side1, side2, side3):
    # Check if triangle is valid
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
        return "Error: Invalid triangle"

    # Calculate angle using Law of Cosines
    numerator = side1**2 + side2**2 - side3**2
    denominator = 2 * side1 * side2
    angle_rad = math.acos(numerator / denominator)
    angle_deg = math.degrees(angle_rad)
    return angle_deg