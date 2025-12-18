"""
QUESTION:
Find the closest pair of points in an array of points using a function called `find_closest_pair` with a time complexity of O(n^2) and without using any additional data structures. Each point is represented as a tuple of two integers. The function should return the closest pair of points.
"""

import math

def find_closest_pair(points):
    def calculate_distance(point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    n = len(points)
    min_distance = math.inf
    closest_pair = None

    for i in range(n):
        for j in range(i+1, n):
            distance = calculate_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair