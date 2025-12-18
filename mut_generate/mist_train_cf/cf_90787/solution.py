"""
QUESTION:
Write a function named `calculate_area` that takes the radius of a circle as input and returns its area. The function should not use the `math` module or any other library that provides a method for calculating the value of pi.
"""

def calculate_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area