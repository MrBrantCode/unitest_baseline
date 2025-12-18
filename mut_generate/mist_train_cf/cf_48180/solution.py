"""
QUESTION:
Design a function named `total_volume` that calculates the total volume of a list of 3D shapes. Each shape is represented by a dictionary containing 'radius', 'height', and 'shape' as keys. The 'shape' key indicates whether the object is a 'cylinder' or a 'cone'. The function should use the mathematical formulas 𝜋𝑟²ℎ for cylinders and 1/3 𝜋𝑟²ℎ for cones to calculate the volume of each shape, then return the total volume of all shapes in the list. The function should take a list of these shape dictionaries as input and return the total volume.
"""

import math

def total_volume(shapes):
    total_vol = 0
    for shape in shapes:
        if shape['shape'] == 'cylinder':
            vol = math.pi * shape['radius']**2 * shape['height']
            total_vol += vol
        elif shape['shape'] == 'cone':
            vol = (1/3) * math.pi * shape['radius']**2 * shape['height']
            total_vol += vol
    return total_vol