"""
QUESTION:
Write a function `calculate_total_distance(points)` that calculates the total distance between consecutive points in a list of 2D coordinates. Each point is a tuple of two integers representing the x and y coordinates. The function should return the total distance as a floating-point number rounded to two decimal places. The input list contains at least two points.
"""

from typing import List, Tuple
import math

def calculate_total_distance(points: List[Tuple[int, int]]) -> float:
    total_distance = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_distance += distance
    return round(total_distance, 2)