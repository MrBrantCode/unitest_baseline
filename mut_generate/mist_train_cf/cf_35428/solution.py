"""
QUESTION:
Implement a function `calculate_polygon_area` that calculates the area of a polygon defined by a set of vertices in a 2D plane. The polygon is represented by a list of points, where each point is defined by its latitude and longitude coordinates in decimal degrees. Use the provided vertices to calculate the area and assume the Earth's radius to be 6371.0 kilometers. The function should return the area of the polygon in square kilometers.

The input is a list of tuples, where each tuple contains two floats representing the latitude and longitude of a vertex. The function should work for any simple polygon (a polygon that does not intersect itself).
"""

from typing import List, Tuple
import math

def calculate_polygon_area(vertices: List[Tuple[float, float]]) -> float:
    R = 6371.0  # Earth's radius in kilometers
    total_area = 0

    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        total_area += (vertices[j][1] - vertices[i][1]) * (vertices[j][0] + vertices[i][0])

    total_area = abs(total_area) / 2.0

    return total_area * (math.pi / 180) * R * R