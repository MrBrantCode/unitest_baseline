"""
QUESTION:
Create a function `calculate_isosceles_triangle_area` that takes four parameters: `side1`, `side2`, `base`, and `allowed_ratio`. The function should calculate the area of an isosceles triangle using Heron's formula if the triangle is valid (i.e., `side1` equals `side2`) and the ratio of `base` to `side1` does not exceed `allowed_ratio`. If either condition is not met, return an error message.
"""

import math

def calculate_isosceles_triangle_area(side1, side2, base, allowed_ratio):
    """
    This function calculates the area of an isosceles triangle using Heron's formula
    and checks if the ratio of the base to the equal sides is not more than a certain ratio.
    If the ratio condition is violated, the function returns a warning message.
    """
    if side1 != side2:
        return "Not an isosceles triangle"

    elif base / float(side1) > allowed_ratio:
        return f"Ratio of base to sides exceeds allowed ratio {allowed_ratio}"

    else:
        #Calculate semiperimeter
        semi_perimeter = (side1 + side2 + base) / 2

        #Calculate area using Heron's formula
        area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * 
                         (semi_perimeter - side2) * (semi_perimeter - base))
        return area