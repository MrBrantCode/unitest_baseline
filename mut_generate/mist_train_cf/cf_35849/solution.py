"""
QUESTION:
Create a function `calculate_sphere_volume` that takes two parameters: `diameter` (a string representing the diameter of the sphere) and `diameter_default` (a float representing the default diameter value). Attempt to convert `diameter` to a float. If successful, calculate the volume using the formula `V = (4/3) * π * (diameter/2)^3` and return the result. If the conversion fails, return `diameter_default`.
"""

import math

def calculate_sphere_volume(diameter, diameter_default):
    try:
        diameter_float = float(diameter)
        volume = (4/3) * math.pi * (diameter_float/2)**3
        return volume
    except ValueError:
        return diameter_default