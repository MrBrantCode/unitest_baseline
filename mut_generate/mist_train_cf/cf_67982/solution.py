"""
QUESTION:
Construct a Python function called `cone_properties` that calculates the lateral surface area and volume of a geometric cone given its radius `r` and height `h`. The function should handle edge cases such as non-positive radius or height, and manage floating point precision issues. It should also be able to handle complex numbers as inputs and calculate the surface area and volume of a truncated cone (frustum) when a second radius `r2` is provided.

The function should return the lateral surface area and volume for a normal cone, and the total surface area and volume for a frustum if `r2` is provided. If the radius or height is zero or negative, the function should return `0` or `None` respectively to indicate an error.
"""

import math

def cone_properties(r, h, r2 = None):
    if type(r) == complex or type(h) == complex:
        r = abs(r)
        h = abs(h)
        if r2:
            r2 = abs(r2)
      
    if r == 0 or h == 0 or (r2 != None and r2 == 0):
        return 0, 0
        
    elif r < 0 or h < 0 or (r2 != None and r2 < 0):
        return None, None
    
    else:
        if r2 is None:
            # Normal cone
            l = math.sqrt(r**2 + h**2)
            lsa = math.pi * r * l
            volume = (1/3) * math.pi * r**2 * h
            return lsa, volume

        else:
            # Frustum
            l = math.sqrt((r-r2)**2 + h**2)
            lsa = math.pi * (r + r2) * l
            area = math.pi * (r**2 + r2**2)
            tsa = lsa + area
            volume = (1/3) * math.pi * h * (r**2 + r2**2 + r*r2)
            return tsa, volume