"""
QUESTION:
Given four distinct points p1, p2, p3, and p4 in a two-dimensional plane, each represented by their coordinates [xi, yi], determine if these points can form a square with four sides of equal positive length and four right angles.

The function name should be `isSquare(p1, p2, p3, p4)`. The input points p1, p2, p3, and p4 are lists of two integers each, where -10^4 <= xi, yi <= 10^4.
"""

def validSquare(p1, p2, p3, p4):
    def distance(p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

    points = [p1, p2, p3, p4]
    dists = []
    for i in range(4):
        for j in range(i + 1, 4):
            dists.append(distance(points[i], points[j]))
    dists.sort()

    return dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[0] < dists[4]