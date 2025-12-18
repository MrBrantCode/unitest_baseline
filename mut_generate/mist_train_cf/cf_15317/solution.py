"""
QUESTION:
Create a function `find_triangle_area` that calculates the total area of a triangle given its base, height, and the lengths of its three sides. The function should first check if the triangle is valid, where a triangle is valid if the sum of the lengths of any two sides is greater than the length of the third side. If the triangle is valid, calculate the area using the formula `(1/2) * base * height`. If the triangle is not valid, return 0.0. The input parameters are the base and height of the triangle, and the lengths of the three sides as floats. The function should return the calculated area as a float.
"""

def find_triangle_area(base: float, height: float, side1: float, side2: float, side3: float) -> float:
    # Check if the triangle is valid
    if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
        # Calculate the area of the triangle
        area = 0.5 * base * height
        return area
    else:
        return 0.0  # Return 0.0 if the triangle is not valid