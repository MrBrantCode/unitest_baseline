"""
QUESTION:
Write a function named `farthest_points` that takes a list of 3D coordinates as input where each coordinate is a string of three integers separated by commas. The function should return a tuple containing the pair of points that are farthest apart and the distance between them. The distance is calculated as the Euclidean distance. The function should consider all possible pairs of points in the input list.
"""

import itertools
import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def farthest_points(coordinates):
    points = [tuple(map(int, point.split(','))) for point in coordinates]
    max_distance = 0
    farthest_pair = ()
    for pair in itertools.combinations(points, 2):
        dist = distance(pair[0], pair[1])
        if dist > max_distance:
            max_distance = dist
            farthest_pair = pair
    return farthest_pair, max_distance