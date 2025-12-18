"""
QUESTION:
Write two functions, `cone_surface_area(r, h)` and `cone_volume(r, h)`, to calculate the lateral surface area and volume of a cone, respectively, given its radius `r` and height `h`. Both `r` and `h` should be positive floating-point numbers. If either `r` or `h` is zero or negative, the functions should return an error message.
"""

import math

def cone_surface_area(r: float, h: float) -> float:
    if r <= 0 or h <= 0:
        return "Radius and Height must be greater than zero."
    l = math.sqrt(r**2 + h**2)    # l is slant height
    return math.pi * r * l

def cone_volume(r: float, h: float) -> float:
    if r <= 0 or h <= 0:
        return "Radius and Height must be greater than zero."
    return (1.0/3) * math.pi * r * r * h