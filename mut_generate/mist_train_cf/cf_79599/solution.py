"""
QUESTION:
Create a function named `cone_properties` that takes in three parameters: `r`, `h`, and `r2` (which is optional and defaults to `None`). The function should calculate the lateral surface area and volume of a cone or frustum of a cone. 

The function should handle edge cases where any of the input parameters are `None` or not instances of `int`, `float`, or `complex`. It should also handle negative or zero inputs by taking the absolute value of `r` and `h`. If `r2` is `None`, the function should calculate the properties of a regular cone; otherwise, it should calculate the properties of a frustum of a cone.
"""

import math
import cmath

def cone_properties(r, h, r2=None):
    # Handles edge cases
    if r is None or h is None or (not isinstance(r, (int, float, complex)) or not isinstance(h, (int, float, complex)) or (r2 is not None and not isinstance(r2, (int, float, complex)))):
        return None, None

    # Handles negative or zero inputs
    r = abs(r)
    h = abs(h)

    l = cmath.sqrt(r**2 + h**2)

    if r2 is None: # If r2 is not provided, calculates for a regular cone
        # Lateral Surface Area
        lsa = math.pi * r * l.real
        # Volume
        volume = (1/3) * math.pi * r**2 * h
    else: # If r2 is provided, calculates for a frustum of a cone
        r2 = abs(r2)
        # Volume
        volume = (1/3) * math.pi * h * (r**2 + r2**2 + r*r2)
        # Lateral Surface Area
        lsa = math.pi * (r + r2) * l.real 

    return lsa, volume