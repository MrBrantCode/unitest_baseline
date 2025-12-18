"""
QUESTION:
Write a function named `calculate_area` that takes the radius of a circle as input and returns the area of the circle. The function must not use the built-in `math` module or any other library that provides a method for calculating the value of pi. Define the value of pi within the function instead.
"""

def calculate_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area