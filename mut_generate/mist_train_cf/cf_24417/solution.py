"""
QUESTION:
Write a function named `distance_3d` that calculates the Euclidean distance between two points in a 3D space. The function should take six parameters: the x, y, and z coordinates of each point. The function should return the calculated distance as a floating-point number.
"""

import math

def distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)