"""
QUESTION:
Create a function `find_circle_area(radius)` that calculates the area of a circle given the radius. The radius should be a positive number (integer or decimal) less than or equal to 10^9. If the radius is not a number, return an error message. If the radius is a decimal, round it to the nearest integer. If the radius is 0, negative, or greater than 10^9, return an error message.
"""

import math

def find_circle_area(radius):
    if isinstance(radius, str):
        return "Invalid input. The radius must be a positive integer or decimal number."
    elif radius <= 0:
        return "Invalid input. The radius must be a positive integer or decimal number."
    elif radius > 10**9:
        return "Invalid input. The radius is too large."

    radius = round(radius)
    area = math.pi * radius**2
    return area