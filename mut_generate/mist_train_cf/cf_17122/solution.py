"""
QUESTION:
Write a function `circleArea` that takes a radius as input and returns the area of a circle using the formula Area = pi * r * r. The radius can be any positive integer between 1 and 10^9 (inclusive). The solution must have a time complexity of O(1) and a space complexity of O(1), and it should only use basic arithmetic operations (+, -, *, /) and the math constant pi.
"""

def circleArea(radius):
    pi = 3.14159
    square_of_radius = radius * radius
    area = pi * square_of_radius
    return area