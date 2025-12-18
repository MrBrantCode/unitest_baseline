"""
QUESTION:
Implement a function named `max_distance_points` that takes a list of at least 2 and at most 1000 tuples representing 2D points in the form (x, y), where x and y are floating-point numbers, and returns a tuple of two tuples representing the pair of points with the maximum Euclidean distance between them. The Euclidean distance is calculated as `sqrt((x2 - x1)^2 + (y2 - y1)^2)`.
"""

from typing import List, Tuple
import math

def max_distance_points(points: List[Tuple[float, float]]) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    max_distance = 0
    max_points = ()
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = math.sqrt((points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2)
            if distance > max_distance:
                max_distance = distance
                max_points = (points[i], points[j])
    
    return max_points