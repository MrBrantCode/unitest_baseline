"""
QUESTION:
Write a function named `calculate_volume` that takes a single argument `radius` and returns the volume of a sphere with the given radius. The function should use the formula 4/3 * π * r^3 and handle cases where the input radius is negative by returning an error message.
"""

import math

def calculate_volume(radius):
    """Function to calculate the volume of a sphere"""
    if radius < 0:
        return "Error: The radius should be a non-negative number!"
    else:
        volume = (4/3) * math.pi * (radius ** 3)
        return volume