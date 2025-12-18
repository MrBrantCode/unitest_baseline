"""
QUESTION:
Calculate the lateral surface area and volume of a cone or frustum of a cone given the radius `r` and height `h`. If the second radius `r2` is provided, the function calculates for a frustum of a cone. The function should handle edge cases, such as negative or zero inputs, and manage floating point precision issues. It should also be able to handle complex numbers as inputs and large inputs without causing a memory overflow. If `r` and `h` are given as a list of complex numbers, the function should return a list of tuples, where each tuple contains the lateral surface area and volume of a cone or frustum of a cone corresponding to the given radius and height.

The function name should be `cone_properties` and it should take three parameters: `r`, `h`, and `r2`. The parameters `r` and `h` are required, while `r2` is optional.
"""

import math
import cmath

def cone_properties(r, h, r2=None):
    # Handles edge cases
    if r is None or h is None or (isinstance(r, (int, float, complex)) is False) or (isinstance(h, (int, float, complex)) is False) or (r2 is not None and isinstance(r2, (int, float, complex)) is False):
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
        lsa = math.pi * (r + r2) * l.real + math.pi * r**2 + math.pi * r2**2
        
    return lsa, volume