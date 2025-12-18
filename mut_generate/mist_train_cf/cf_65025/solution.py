"""
QUESTION:
Create a function `calc_volume(r, h)` that calculates the volume of a cylinder given its radius `r` and height `h`. The function should return the calculated volume. The radius and height should be provided as input parameters to the function.
"""

import math

def calc_volume(r, h):
    # Correct formula for cylinder volume
    volume = math.pi * r**2 * h
    return volume