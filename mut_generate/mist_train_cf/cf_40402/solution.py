"""
QUESTION:
Implement a function `k_closest_points` that takes a list of 2D points, a reference point, and the value of k as input, and returns a list of the k closest points to the reference point. The function should use Euclidean distance to calculate the distance between points and return the k points with the smallest distances.
"""

from typing import List, Tuple
import math

def k_closest_points(points: List[Tuple[int, int]], reference: Tuple[int, int], k: int) -> List[Tuple[int, int]]:
    distances = [(math.sqrt((point[0] - reference[0])**2 + (point[1] - reference[1])**2), point) for point in points]
    distances.sort(key=lambda x: x[0])
    return [point for _, point in distances[:k]]