"""
QUESTION:
Write a Python function `tetrahedron_volume_and_type` that takes four 3D points as input and returns the volume of the tetrahedron formed by these points and a boolean indicating whether the tetrahedron is regular or irregular. A regular tetrahedron has all its edges equal. The function should handle possible floating point precision problems. The input points are represented as tuples of three floats.
"""

import math
from itertools import combinations

def tetrahedron_volume_and_type(points):
    # calculate the volume using the formula
    (x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4) = points
    volume = abs(x1 * y2 * z3 + x2 * y3 * z4 + x3 * y4 * z1 + x4 * y1 * z2 -
                 x4 * y2 * z3 - x1 * y3 * z4 - x2 * y4 * z1 - x3 * y1 * z2) / 6
    
    # calculate all the six distances
    def dist(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
    
    distances = [dist(p1, p2) for p1, p2 in combinations(points, 2)]
    is_regular = len(set(round(d, 5) for d in distances)) == 1
    
    return round(volume, 5), is_regular