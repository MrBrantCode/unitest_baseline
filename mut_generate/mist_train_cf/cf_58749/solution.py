"""
QUESTION:
Write a function `numberOfIsoscelesTriangles(points)` that takes a list of points in the plane as input, where each point is represented as a list of two integers `[x, y]`, and returns the number of unique isosceles triangles that can be formed using these points. The function should have a time complexity of O(n^2 log n) or better, where n is the number of points. The input list `points` has the following constraints: `1 <= n <= 500`, `points[i].length == 2`, and `-10^4 <= x, y <= 10^4`.
"""

import collections
import itertools
import operator

def numberOfIsoscelesTriangles(points):
    storeDistance = collections.defaultdict(list)
    for i, (x1, y1) in enumerate(points):
        for j, (x2, y2) in enumerate(points):
            if i < j:
                dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
                storeDistance[(i, j)] = dist
                storeDistance[(j, i)] = dist
    isoscelesTriangles = 0
    for i in range(len(points)):
        distances = sorted((distance, point2) for (point1, point2), distance in storeDistance.items() if point1 == i)
        groups = itertools.groupby(distances, key=operator.itemgetter(0))
        for _, group in groups:
            group_list = list(group)
            cnt = collections.Counter([point2 for _, point2 in group_list])
            isoscelesTriangles += sum([c * (c - 1) // 2 for c in cnt.values()])
    return isoscelesTriangles