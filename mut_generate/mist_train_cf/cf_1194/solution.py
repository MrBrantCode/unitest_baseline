"""
QUESTION:
Write a function named `calculate_volume` that calculates the volume of a sphere given a radius `r` without using the formula V = (4/3) * π * r^3. The function should be able to handle cases where the radius is a decimal number and return the volume rounded to the nearest integer value.
"""

import math

def calculate_volume(radius):
    step = 0.001  # Integration step size
    volume = 0

    for x in range(int(radius * 1000)):
        # Numerical integration
        height = math.sqrt(radius**2 - (x/1000)**2)
        area = math.pi * height * 2 * (x/1000)
        volume += area * step

    return round(volume)