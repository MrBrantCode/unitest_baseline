"""
QUESTION:
Create a function `find_triangle_area` that calculates the total area of a triangle given its base, height, and the lengths of its three sides. The function should check if the input values are numeric and non-negative, and if the triangle is valid (i.e., the sum of the lengths of any two sides is greater than the length of the third side). If any of these conditions are not met, the function should return an error message. The function should be able to handle decimal input for the base, height, and side lengths. The function should return the area of the triangle if it is valid, and an error message otherwise.
"""

from typing import Union

def find_triangle_area(base: float, height: float, side1: float, side2: float, side3: float) -> Union[float, str]:
    if not all(isinstance(val, (int, float)) for val in [base, height, side1, side2, side3]):
        return "Error: Input values must be numeric"
    
    if any(val < 0 for val in [side1, side2, side3]):
        return "Error: Side lengths cannot be negative"
    
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Error: Invalid triangle"
    
    area = 0.5 * base * height
    return area