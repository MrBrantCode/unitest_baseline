"""
QUESTION:
Write a function isConvex that takes a list of at least 3 points (x, y) in the range -10,000 to 10,000 as input, representing the vertices of a simple polygon in order, and returns True if the polygon is convex and False otherwise.
"""

def isConvex(points):
    n = len(points)
    edges = [(points[i+1][0] - points[i][0], points[i+1][1] - points[i][1]) for i in range(n-1)]
    edges.append((points[0][0] - points[n-1][0], points[0][1] - points[n-1][1]))  # add edge from last point to first point
    cross_products = [edges[i][0]*edges[i+1][1] - edges[i][1]*edges[i+1][0] for i in range(n-1)]
    cross_products.append(edges[n-1][0]*edges[0][1] - edges[n-1][1]*edges[0][0])  # add cross product for last edge with first edge
    return all(cp >= 0 for cp in cross_products) or all(cp <= 0 for cp in cross_products)