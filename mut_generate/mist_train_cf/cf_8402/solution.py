"""
QUESTION:
Create a function called "frustrum_volume" that takes three parameters: base_radius (float), top_radius (float), and height (float) and returns the volume of the frustrum (float). The function should use the correct formula for calculating the volume of a frustrum, which is a 3D shape formed by cutting off the top of a cone with a plane parallel to its base. The formula for the volume of a frustrum is: V = (1/3) * π * h * (R^2 + r^2 + R*r), where h is the height of the frustrum, R is the base radius, and r is the top radius.
"""

import math

def frustrum_volume(base_radius, top_radius, height):
    return (1/3) * math.pi * height * (base_radius**2 + top_radius**2 + base_radius*top_radius)