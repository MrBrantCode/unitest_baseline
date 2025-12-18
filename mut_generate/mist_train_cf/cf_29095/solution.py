"""
QUESTION:
Implement the function `find_nearest_point(pivot, points)` that finds the nearest point to a given target point and calculates the distance between them. The function takes two parameters:
- `pivot`: a tuple representing the target point (x, y) coordinates.
- `points`: a list of tuples, each representing a point's (x, y) coordinates.

The function should return a tuple containing the nearest point's coordinates and the distance between the nearest point and the target point, calculated using the Euclidean distance formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
"""

import math

def find_nearest_point(pivot, points):
    nearest = None
    dist = float('inf')  # Initialize with positive infinity
    for point in points:
        temp_dist = math.sqrt((point[0] - pivot[0])**2 + (point[1] - pivot[1])**2)
        if temp_dist < dist:
            nearest = point
            dist = temp_dist
    return (nearest, dist)