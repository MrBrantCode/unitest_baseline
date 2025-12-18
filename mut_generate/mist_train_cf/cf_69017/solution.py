"""
QUESTION:
Create a function named `sphere_volume(r)` that takes a single argument `r` representing the radius of a sphere and returns the volume of the sphere using the formula `V = 4/3 * π * r^3`. The function should import the math module for the value of π and handle the calculation internally. The input `r` is expected to be a numeric value, and the output should be the calculated volume of the sphere.
"""

import math

def sphere_volume(r):
    cube_radius = pow(r, 3)
    volume = ((4/3) * math.pi * cube_radius)
    return volume