"""
QUESTION:
Write a function named `convert` that takes an angle in minutes of arc as input and returns the equivalent angle in radians. The conversion should account for the fact that there are 60 minutes of arc in a degree and 2π radians in a degree (or π/180 radians in a degree).
"""

import math

def convert(arc_minutes):
    # There are 60 arc minutes in a degree and 2*pi radians in a degree, so we can simply divide by 
    # these values to get our result.
    degrees = arc_minutes / 60.0
    radians = degrees * (math.pi / 180.0)
    return radians