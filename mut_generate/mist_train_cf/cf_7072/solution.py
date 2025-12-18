"""
QUESTION:
Compute the surface area of a frustum of a pyramid given the base area, top area, and height. The function should be named `frustum_surface_area` and should take three parameters: `base_area`, `top_area`, and `height`, all in the same units. Assume the base shape is a circle.
"""

import math

def frustum_surface_area(base_area, top_area, height):
    r1 = math.sqrt(base_area / math.pi)
    r2 = math.sqrt(top_area / math.pi)
    l = math.sqrt(height**2 + (r1 - r2)**2)
    lateral_surface_area = math.pi * (r1 + r2) * l
    total_surface_area = lateral_surface_area + top_area + base_area
    return total_surface_area