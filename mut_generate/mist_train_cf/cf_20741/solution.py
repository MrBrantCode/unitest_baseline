"""
QUESTION:
Write a function named `calculate_area` that takes three positive real numbers `a`, `b`, and `c` as input and returns the area of a triangle with side lengths `a`, `b`, and `c`. The function should have a time complexity of O(1) and handle the case where the given lengths cannot form a valid triangle by returning an error message.
"""

import math

def calculate_area(a, b, c):
    # Check if the given lengths can form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "The given lengths do not form a valid triangle."

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area