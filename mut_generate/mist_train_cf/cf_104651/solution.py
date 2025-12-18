"""
QUESTION:
Create a function named `calculate_circle_area` that takes one argument, the radius of a circle in centimeters, and returns the area of the circle rounded to the nearest integer. The function should use the formula `pi * r^2` to calculate the area, where `r` is the radius.
"""

import math

def calculate_circle_area(radius):
    return round(math.pi * radius ** 2)