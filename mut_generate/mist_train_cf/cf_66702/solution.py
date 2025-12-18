"""
QUESTION:
Create a function called `calculate_area` that takes three arguments representing the lengths of a triangle's sides. The function should return a string describing the type of triangle (equilateral, isosceles, scalene) and its area, rounded to two decimal places, if the side lengths form a valid triangle and are positive. If the side lengths are not valid (i.e., non-positive or do not satisfy the triangle inequality), return an error message.
"""

import math

def calculate_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Error: Side lengths must be positive."
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "Error: The given side lengths do not form a triangle."
    
    # Determine the type of triangle
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or c == a:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Apply Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return f"The triangle is {triangle_type} and its area is {area:.2f} square units."