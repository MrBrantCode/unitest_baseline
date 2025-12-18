"""
QUESTION:
Implement a function `polygon_area(vertices)` that calculates the area of a closed polygon defined by a set of vertices. The function takes a list of (x, y) coordinate pairs in counter-clockwise order as input and returns the area of the polygon using the shoelace formula. The shoelace formula is given by: Area = 0.5 * |(x1y2 + x2y3 + ... + xn-1yn + xny1) - (y1x2 + y2x3 + ... + yn-1xn + ynx1)|.
"""

def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[i][1] * vertices[j][0]
    area = abs(area) / 2.0
    return area