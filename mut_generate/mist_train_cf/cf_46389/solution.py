"""
QUESTION:
Develop a function `sector_area(radius, angle)` that calculates the surface area of a circular sector given the radius and central angle in degrees. The function should return the surface area as a floating-point number, but return `None` if the central angle exceeds 360 degrees.
"""

import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    else:
        return (angle/360.0) * math.pi * radius**2