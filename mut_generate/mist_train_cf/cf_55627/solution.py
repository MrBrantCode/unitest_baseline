"""
QUESTION:
Create a function called `sphere_volume(radius)` that calculates the volume of a sphere given its radius. The function should return the volume of the sphere using the formula `(4/3) * pi * r^3`.
"""

import math

def sphere_volume(radius):
    volume = (4.0/3) * math.pi * (radius**3)
    return volume