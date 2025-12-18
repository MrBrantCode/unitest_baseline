"""
QUESTION:
Create a function named `calculate_frustrum_volume` that calculates the volume of a frustrum, a cone with the top cut off by a plane parallel to the base. The function should take three parameters: `base_radius` and `top_radius` as floats representing the radii of the base and top of the frustrum, respectively, and `height` as a float representing the height of the frustrum. The function should return the volume of the frustrum as a float.
"""

import math

def calculate_frustrum_volume(base_radius, top_radius, height):
    volume = (1/3) * math.pi * height * (base_radius**2 + base_radius*top_radius + top_radius**2)
    return volume