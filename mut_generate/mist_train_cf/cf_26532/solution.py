"""
QUESTION:
Implement a function `calculatePolygonArea(vertices)` that calculates the area of a 2D polygon given its vertices. The function takes a list of 2D points in the form of (x, y) coordinates as input and returns the area of the polygon formed by these vertices. The input list of vertices forms a valid polygon with at least 3 vertices.
"""

from typing import List, Tuple

def entance(vertices: List[Tuple[float, float]]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to the first vertex for the last iteration
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0