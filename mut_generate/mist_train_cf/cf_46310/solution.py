"""
QUESTION:
Write a function `calculate_sphere_volume` that takes the diameter of a sphere as input and returns its volume, given by the formula V = 4/3 * π * r³, where r is the radius of the sphere (half the diameter).
"""

import math

def calculate_sphere_volume(diameter):
    radius = diameter / 2
    return 4/3 * math.pi * (radius ** 3)