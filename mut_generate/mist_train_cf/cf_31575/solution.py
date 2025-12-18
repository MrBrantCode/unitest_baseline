"""
QUESTION:
Implement a function `calculate_polygon_area(vertices)` that calculates the area of a 2D polygon given its vertices. The function takes a list of 2D points (tuples of two floats) in clockwise or counterclockwise order as input and returns the area of the polygon as a float.
"""

from typing import List, Tuple

def calculate_polygon_area(vertices: List[Tuple[float, float]]) -> float:
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0