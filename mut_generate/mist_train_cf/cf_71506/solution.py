"""
QUESTION:
Write a function called `torus_volume` that calculates the volume of a torus given two parameters, `r` and `a`, which represent the radius from the center of the hole to the center of the tube and the radius of the tube itself, respectively. The function should return the volume of the torus as a floating-point number. The formula for the volume of a torus is `V = 2 * pi^2 * r * a^2`.
"""

import math

def torus_volume(r, a):
    return 2 * math.pi**2 * r * a**2