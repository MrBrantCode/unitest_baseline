"""
QUESTION:
Implement a function `findExtremePoints` that takes a list of 2D points as input, where each point is represented as a pair of integers (x, y), and returns a list of extreme points that form the convex hull in counter-clockwise order. The function should handle cases where the number of points is less than 3. The points in the output list should define the shape of the smallest convex polygon that contains all the input points.
"""

def findExtremePoints(points):
    n = len(points)
    if n < 3:
        return points

    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i

    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if (points[i][1] - points[p][1]) * (points[q][0] - points[p][0]) - (points[i][0] - points[p][0]) * (points[q][1] - points[p][1]) > 0:
                q = i
        p = q
        if p == l:
            break

    return hull