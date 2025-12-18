"""
QUESTION:
Develop a function named `cone_properties` that calculates the lateral surface area and volume of a cone given the radius `r` and height `h`. The function should handle edge cases where the radius or height is zero or negative and manage floating point precision issues. It should also be able to handle large inputs without causing a memory overflow. The function should return the lateral surface area and volume as a pair of values. The formulas for the lateral surface area and volume of a cone are π*r*l and (1/3)*π*r^2*h, respectively, where l is the slant height of the cone calculated using the Pythagorean theorem as sqrt(r^2 + h^2).
"""

import math

def cone_properties(r, h):
    if r <= 0 or h <= 0:
        return "Invalid input: Radius and height must be greater than zero."
    
    # Calculate slant height
    l = math.sqrt(math.pow(r, 2) + math.pow(h, 2))

    # Lateral Surface Area = πrl
    lsa = math.pi * r * l

    # Volume = 1/3*πr^2h
    volume = (1/3) * math.pi * math.pow(r, 2) * h
    
    return round(lsa, 2), round(volume, 2)