"""
QUESTION:
Write a function `max_distance_between_points` that takes a list of 3D points as input, where each point is a triplet of integers, and returns the pair of points with the maximum Euclidean distance between them. If there are multiple pairs with the same maximum distance, return any one of them.
"""

import itertools
import math

def max_distance_between_points(points):
    def distance(point1, point2):
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

    max_dist = 0
    max_pair = ()
    for pair in itertools.combinations(points, 2):
        dist = distance(pair[0], pair[1])
        if dist > max_dist:
            max_dist = dist
            max_pair = pair
    return max_pair