"""
QUESTION:
Write a function `is_inside_polygon(polygon, N, point)` that takes in a list of tuples `polygon` representing the vertices of the polygon, an integer `N` representing the number of vertices in the polygon, and a tuple `point` containing the x and y coordinates of the point to be checked. The function should return `True` if the point is inside the polygon and `False` otherwise.
"""

def entrance(polygon, N, point):
    x, y = point
    inside = False
    p1x, p1y = polygon[0]
    for i in range(N+1):
        p2x, p2y = polygon[i % N]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside