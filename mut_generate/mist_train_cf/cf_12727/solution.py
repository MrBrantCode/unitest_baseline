"""
QUESTION:
Write a function named `closest_pair` that takes an array of points as input and returns the closest pair of points without using any additional data structures. The function should have a time complexity of O(n^2). Each point is represented as a pair of coordinates (x, y). If the input array contains less than 2 points, the function should return None.
"""

import math

def closest_pair(points):
    n = len(points)
    if n < 2:
        return None

    min_dist = float('inf')
    closest_points = None

    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

            if dist < min_dist:
                min_dist = dist
                closest_points = (points[i], points[j])

    return closest_points