"""
QUESTION:
Write a function named `triangle_area` that takes three arguments `a`, `b`, and `c` representing the sides of a triangle and returns the area of the triangle accurate to four decimal places. 

The function should first validate the sides by checking if they are positive and if the sum of any two sides exceeds the third side. If the sides do not form a valid triangle, the function should return `None` along with an error message. 

Additionally, if the calculated area is less than 0.0001, the function should return a warning message. The area calculation should utilize Heron's formula.
"""

import math

def triangle_area(a, b, c):
    # Check to see if the sides are positive and create a valid triangle
    if a <= 0 or b <= 0 or c <= 0:
        print("Sides of a triangle must be positive.")
        return None
    if a + b <= c or a + c <= b or b + c <= a:
        print("The sum of any two sides of a triangle must exceed the third side.")
        return None

    # Calculate the semi-perimeter
    p = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 4)

    # Check for minuscule area
    if area < 0.0001:
        return "Warning: The area of the triangle is very small."

    return area