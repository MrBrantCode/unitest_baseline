"""
QUESTION:
Write a function named `calculateCumulativeDistance` that takes a list of 3-dimensional Cartesian coordinate tuples and returns the cumulative Euclidean distance traversed when moving from the first coordinate to the last, passing through each intermediate coordinate in the sequence. The Euclidean distance between two points (x1, y1, z1) and (x2, y2, z2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2).
"""

from typing import List, Tuple
from math import sqrt, pow

def calculateCumulativeDistance(points: List[Tuple[float, float, float]]) -> float:
    """Calculates the cumulative Euclidean distance traversed when moving from the first coordinate to the last."""
    
    def calculateEuclideanDistance(p1: Tuple[float, float, float], 
                                   p2: Tuple[float, float, float]) -> float:
        """Calculates the Euclidean distance between two points."""
        return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2) + pow(p2[2] - p1[2], 2))
    
    distance = 0
    
    for i in range(len(points) - 1):
        distance += calculateEuclideanDistance(points[i], points[i + 1])
    
    return distance