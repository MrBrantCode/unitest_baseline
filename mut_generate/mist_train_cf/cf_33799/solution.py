"""
QUESTION:
Write a function `calculate_distances(points)` that takes a list of tuples `points` representing 2D coordinates and returns a 2D list of distances between each pair of points, calculated using the Euclidean distance formula. The returned distances should be rounded to 15 decimal places. The input list `points` contains tuples of (x, y) coordinates.
"""

import math

def calculate_distances(points):
    n = len(points)
    distances = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            distances[i][j] = round(distance, 15)
            distances[j][i] = round(distance, 15)

    return distances