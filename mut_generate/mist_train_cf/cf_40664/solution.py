"""
QUESTION:
Implement a function `calculatePolygonArea` that calculates the area of a simple polygon. The function takes a list of tuples representing the vertices of the polygon in a two-dimensional plane, ordered either clockwise or counterclockwise, and returns the area of the polygon. The polygon is assumed to be non-self-intersecting.
"""

def calculatePolygonArea(vertices):
    area = 0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)

    return abs(area) / 2