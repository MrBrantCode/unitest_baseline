"""
QUESTION:
Write a function `euclidean_distance(p1, p2)` to compute the Euclidean distance between two points `p1` and `p2` in a 2D plane, where `p1` and `p2` are tuples of decimal numbers representing the coordinates of the points. The function should return the distance rounded to two decimal places.
"""

import math

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return round(distance, 2)