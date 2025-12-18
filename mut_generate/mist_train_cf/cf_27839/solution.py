"""
QUESTION:
Write a function `shortest_distance(vertices)` that takes a list of 3D vertex coordinates in the format "VRTX id x y z" and returns a tuple containing the identifiers of the two vertices with the shortest Euclidean distance between them.

- The input list `vertices` contains n lines, each representing a vertex where id is an integer identifier and x, y, z are floating-point coordinates.
- The function should return a tuple containing the identifiers of the two vertices with the shortest distance between them.
"""

from typing import List, Tuple
import math

def shortest_distance(vertices: List[str]) -> Tuple[int, int]:
    def calculate_distance(vertex1, vertex2):
        x1, y1, z1 = map(float, vertex1.split()[2:])
        x2, y2, z2 = map(float, vertex2.split()[2:])
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    min_distance = float('inf')
    min_vertices = (0, 0)
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            distance = calculate_distance(vertices[i], vertices[j])
            if distance < min_distance:
                min_distance = distance
                min_vertices = (int(vertices[i].split()[1]), int(vertices[j].split()[1]))
    return min_vertices