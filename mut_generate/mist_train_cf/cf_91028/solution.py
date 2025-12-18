"""
QUESTION:
Write a function `calculate_sphere_volume` to calculate the volume of a sphere given a radius `r` using the formula V = (4/3) * π * r^3, and return the volume as a floating-point number. The input `r` is a non-negative number.
"""

import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume