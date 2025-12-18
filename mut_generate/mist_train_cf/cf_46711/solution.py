"""
QUESTION:
Write a function `closest_points_to_origin` that takes a list of points and an integer k as input. Each point is represented as a tuple of two integers. The function should return the k points in the list that are closest to the origin (0,0) based on Euclidean distance.
"""

import math

def closest_points_to_origin(points, k):
    points.sort(key=lambda point: math.sqrt(point[0]**2 + point[1]**2))
    return points[:k]