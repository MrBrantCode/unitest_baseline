"""
QUESTION:
Create a function `calc_volume` that calculates the volume of a 3D shape. The function should take a required `type` parameter and additional keyword arguments specific to the shape type. The shape types and their required parameters are:
- "cube": side
- "sphere": radius
- "cylinder": radius and height
The function should use the standard formulas for the volume of each shape and return the calculated volume.
"""

import math

def calc_volume(type, **kwargs):
    if type == "cube":
        return kwargs['side'] ** 3
    elif type == "sphere":
        return 4/3 * math.pi * (kwargs['radius'] ** 3)
    elif type == "cylinder":
        return math.pi * (kwargs['radius'] ** 2) * kwargs['height']