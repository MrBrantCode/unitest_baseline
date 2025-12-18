"""
QUESTION:
Write a function named `calculate_sphere_volume` that takes one argument, the radius of a sphere. The function should return the volume of the sphere using the formula V = (4/3) * π * r^3.
"""

import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume