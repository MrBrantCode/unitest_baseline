"""
QUESTION:
Implement a function `closest_pair(points, distance)` that finds the closest pair of points based on a given distance function. The function takes two parameters: `points`, a list of tuples representing points in a 2D plane, each with coordinates and a unique label, and `distance`, a function that calculates the distance between two points. The function should return the pair of points that are closest to each other based on the given distance function.
"""

import math

def closest_pair(points, distance):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])
    return closest_pair