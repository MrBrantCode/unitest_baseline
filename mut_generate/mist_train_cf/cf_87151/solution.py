"""
QUESTION:
Create a function `compute_triangle_area_and_perimeter(a, b, c)` that takes the lengths of three sides of a triangle as input. The function should return the area and perimeter of the triangle, calculated using the Law of Cosines, if the triangle is valid. A valid triangle is defined as a triangle where the sum of any two sides is greater than the third side. If the triangle is not valid, return an error message.
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