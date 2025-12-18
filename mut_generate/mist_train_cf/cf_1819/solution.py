"""
QUESTION:
Write a function `compute_triangle_area_and_perimeter(a, b, c)` that takes the lengths of the three sides of a triangle as input and returns the area and perimeter of the triangle. The function should use the Law of Cosines to calculate the area and should first check if the triangle is valid (i.e., the sum of any two sides is greater than the third side). If the triangle is not valid, the function should return an error message. The function should return both the area and the perimeter, or the error message if the triangle is not valid.
"""

import math

def compute_triangle_area_and_perimeter(a, b, c):
    # Check if the triangle is valid
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid triangle: sum of any two sides must be greater than the third side"

    # Compute the area using the Law of Cosines
    area = 0.25 * math.sqrt((a**2 + b**2 + c**2)**2 - 2*(a**4 + b**4 + c**4))

    # Compute the perimeter
    perimeter = a + b + c

    return area, perimeter