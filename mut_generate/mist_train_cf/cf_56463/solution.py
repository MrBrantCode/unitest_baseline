"""
QUESTION:
Calculate the radius of a sphere given its volume. The formula for the volume of a sphere is V = (4/3)πr³. Create a function `calculate_radius` that takes the volume as input and returns the radius. The input volume is in cubic centimeters and the output radius should be in centimeters.
"""

import math

def calculate_radius(volume):
    radius = ((3*volume) / (4*math.pi))**(1/3)
    return radius