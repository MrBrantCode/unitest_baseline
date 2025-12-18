"""
QUESTION:
Create a program with a `main` function that repeatedly prompts the user to input the lengths of the sides of a triangle and calculates the area of the triangle using Heron's formula. The program should validate the user's input to ensure it forms a valid triangle and handle any potential exceptions or errors. The program should round the calculated area to two decimal places and provide an option for the user to choose whether they want to calculate the area of another triangle or exit the program.

The `main` function should use two helper functions: `calculate_area(a, b, c)` to calculate the area of the triangle given the side lengths `a`, `b`, and `c`, and `validate_triangle(a, b, c)` to check if the input forms a valid triangle. The `main` function should continue to prompt the user until they choose to exit.
"""

import math

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 2)

def validate_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True