"""
QUESTION:
Write a function named `calculate_sphere_volume` that takes the radius `r` as input and returns the volume of a sphere with the given radius. The volume should be calculated using the formula `(4/3) * Pi * r^3`.
"""

import math

def calculate_sphere_volume(r):
    return (4.0/3) * math.pi * math.pow(r, 3)