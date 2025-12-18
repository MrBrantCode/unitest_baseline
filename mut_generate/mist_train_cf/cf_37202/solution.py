"""
QUESTION:
Implement the function `constructRNG(points)` that takes a list of 2D points as input and returns the adjacency list representation of the Relative Neighborhood Graph (RNG) for the given set of points. In the RNG, each point is connected to all other points that are not closer to it than any other point.

Restrictions:
- Each point is a tuple of two integers representing its x and y coordinates.
- The input list contains at least two points.
- The function should return a dictionary where each key is a point and its corresponding value is a list of neighboring points in the RNG.
"""

from math import sqrt

def relative_neighborhood_graph(points):
    def distance(p1, p2):
        return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    rng = {}
    for p in points:
        rng[p] = []
        for q in points:
            if p != q:
                is_neighbor = True
                for r in points:
                    if r != p and r != q:
                        if distance(p, r) < distance(p, q) and distance(q, r) < distance(p, q):
                            is_neighbor = False
                            break
                if is_neighbor:
                    rng[p].append(q)
    return rng