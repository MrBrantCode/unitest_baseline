"""
QUESTION:
Create a function named `extended_area_triangle(a, b, c)` that takes the lengths of the three edges of a triangle as input. The function should return a tuple containing the area of the triangle calculated via Heron's theorem, the triangle's classification (scalene, isosceles, or equilateral), and the triangle's perimeter. The edge lengths must be natural numbers. If the inputs do not form a proper triangle (i.e., the sum of any two lengths is not greater than the third), return -1. The area should be rounded to two decimal places.
"""

def extended_area_triangle(a, b, c):
    # Check if the inputs are natural numbers and the triangle condition
    if not all(isinstance(i, int) and i > 0 for i in (a, b, c)) or (a + b <= c or a + c <= b or b + c <= a):
        return -1

    # Classify the triangle
    classification = 'Equilateral' if a == b == c else 'Isosceles' if a == b or a == c or b == c else 'Scalene'

    # Compute the perimeter
    perimeter = a + b + c

    # Compute the semi-perimeter
    s = perimeter / 2

    # Compute the area using Heron's formula
    area = round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)

    return area, classification, perimeter