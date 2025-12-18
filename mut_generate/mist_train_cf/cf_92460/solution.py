"""
QUESTION:
Write a function named `closest_pair` that finds the closest pair of points in a given array of points without using any additional data structures. The function should have a time complexity of O(n^2), where n is the number of points in the array. The input is an array of points, where each point is represented as a pair of coordinates (x, y). The function should return the pair of points with the minimum distance between them. If the input array contains less than 2 points, the function should return None.
"""

import math

def closest_pair(points):
    n = len(points)
    if n < 2:
        return None

    min_dist = float('inf')
    closest_points = None

    # Iterate over all pairs of points
    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

            # Update minimum distance and closest pair of points if necessary
            if dist < min_dist:
                min_dist = dist
                closest_points = (points[i], points[j])

    return closest_points