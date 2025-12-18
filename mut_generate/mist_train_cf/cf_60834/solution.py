"""
QUESTION:
Write a function called `sphere_volume(radius)` that calculates the volume of a sphere given its radius `r`. The function should use the formula `V = 4/3*pi*r^3` and include error handling to ensure the input is a non-negative number. If the input is invalid, the function should raise an exception. The implementation should be able to handle large number inputs efficiently.
"""

import math

def sphere_volume(radius):
    if type(radius) not in [int, float] or radius < 0:
        raise Exception("The radius of a sphere can't be negative and must be a number.")
    return (4/3) * math.pi * radius**3