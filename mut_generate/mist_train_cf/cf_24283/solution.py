"""
QUESTION:
Write a function named `calculate_area_triangle` that takes three arguments `a`, `b`, and `c` representing the side lengths of a triangle. Calculate and return the area of the triangle using Heron's formula. The function should handle valid triangle side lengths (i.e., the sum of any two side lengths is greater than the third side length) and return the area as a float value.
"""

def calculate_area_triangle(a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5