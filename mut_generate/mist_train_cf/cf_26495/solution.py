"""
QUESTION:
Write a function `calculate_distances(coordinates)` that calculates the Euclidean distance between each pair of coordinates in the input list `coordinates`. The input list will contain at least two tuples, each with exactly two integers representing x and y coordinates. Return a list of these distances.
"""

import math

def calculate_distances(coordinates):
    distances = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distances.append(distance)
    return distances