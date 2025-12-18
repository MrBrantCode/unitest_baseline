"""
QUESTION:
Design a function named `get_distance` to calculate the Euclidean distance between two points in a 3-D space, given the coordinates of the two points as input. Each point's coordinates should be passed as a tuple of three integers or floats representing the x, y, and z coordinates. The function should return the distance as a float.
"""

def get_distance(p1, p2):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    dist = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
    return dist