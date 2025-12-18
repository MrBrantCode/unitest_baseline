"""
QUESTION:
Write a function named `triangle_properties` that takes three arguments `a`, `b`, and `c` representing the lengths of the sides of a triangle. The function should return a tuple containing the area and type of the triangle (equilateral, isosceles, or scalene) to a precision of 2 decimal points if the sides can form a valid triangle. A triangle is valid if the sum of each pair of sides is greater than the length of the remaining side. If the sides cannot form a valid triangle, return -1.
"""

import math

def triangle_properties(a, b, c):
    # Check if the triangle is valid
    if (a + b > c) and (b + c > a) and (c + a > b):
        # Classify the triangle
        if a == b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or c == a:
            triangle_type = "Isosceles"
        else:
            triangle_type = "Scalene"
        
        # Heron's formula to calculate area
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2), triangle_type
    else:
        # The triangle is invalid
        return -1