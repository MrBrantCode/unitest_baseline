"""
QUESTION:
Write a function `circleArea` that calculates the area of a circle given its radius, using the formula Area = pi * r * r, where r is the radius of the circle. The radius can be any positive integer. The function should only use basic arithmetic operations (+, -, *, /) and the math constant pi. It should not use any pre-defined functions like pow or sqrt. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def circleArea(radius):
    pi = 3.14159
    square_of_radius = radius * radius
    area = pi * square_of_radius
    return area