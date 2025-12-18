"""
QUESTION:
Implement a `calculate_area` method that calculates the area of a polygon using the Shoelace formula, given a list of vertices where each vertex is represented by its x and y coordinates. The method should return the calculated area. The input list of vertices is guaranteed to have at least three elements and forms a closed polygonal chain.
"""

def calculate_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = abs(area) / 2
    return area