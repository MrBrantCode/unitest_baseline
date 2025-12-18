"""
QUESTION:
Implement the function `calculate_exterior_length(points)` to calculate the exterior length of a polygon given its vertices, where `points` is a list of tuples representing 2D points in the form (x, y). The function should return the total exterior length of the polygon. Assume the input list has at least two points.
"""

import math

def calculate_exterior_length(points):
    total_length = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]  # Wrap around to the first point for the last edge
        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_length += length

    return total_length