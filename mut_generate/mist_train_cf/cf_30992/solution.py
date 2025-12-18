"""
QUESTION:
Implement a function `calculate_polygon_area(vertices)` that calculates the area of a 2D polygon given its vertices. The function takes a list of 2D points representing the vertices of a polygon, where each point is a tuple of two numbers (x, y), and the vertices are listed in clockwise or counterclockwise order. The function should return the area of the polygon as a floating-point number.
"""

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to the first vertex for the last edge
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0