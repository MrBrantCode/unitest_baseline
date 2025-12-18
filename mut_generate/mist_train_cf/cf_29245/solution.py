"""
QUESTION:
Implement a function `calculate_polygon_area(vertices: List[Tuple[float, float]]) -> float` to calculate the area of a polygon given its vertices. The input is a list of tuples, where each tuple contains the x and y coordinates of a vertex. The function should return 0 if the input list contains less than 3 vertices.
"""

from typing import List, Tuple

def calculate_polygon_area(vertices: List[Tuple[float, float]]) -> float:
    if len(vertices) < 3:
        return 0

    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]

    area = abs(area) / 2
    return area