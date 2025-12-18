"""
QUESTION:
Write a function called `calculate_torus_volume` to calculate the volume of a torus. The function should take two arguments: `r`, the radius of the tube, and `R`, the distance from the center of the tube to the center of the torus. The formula for the volume is `(pi * r^2) * (2 * pi * R)`.
"""

import math

def calculate_torus_volume(r, R):
    return (math.pi * r**2) * (2 * math.pi * R)