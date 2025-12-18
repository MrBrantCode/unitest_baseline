"""
QUESTION:
Design a Python function `compute_volume(cylinders)` that takes a list of dictionaries, where each dictionary represents a cylinder with 'radius' and 'height' as required keys, and returns the total volume of all cylinders in the list. The volume of a cylinder is calculated as π*r^2*h, where r = radius and h = height.
"""

import math

def compute_volume(cylinders):
    total_volume = 0
    for cylinder in cylinders:
        radius = cylinder['radius']
        height = cylinder['height']
        volume = math.pi * (radius ** 2) * height
        total_volume += volume
    return total_volume