"""
QUESTION:
Develop a function named `euclidean_distance_3d` that calculates the Euclidean distance between two points in a 3D space. The function should take two tuples of three numbers each as input, representing the x, y, and z coordinates of the two points, and return the Euclidean distance between them.
"""

import math

def euclidean_distance_3d(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)