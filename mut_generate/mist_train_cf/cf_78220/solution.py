"""
QUESTION:
Given a set of distinct coordinates in the xy-plane, write a function `minAreaRect(points)` that calculates the smallest possible area of a rectangle that can be constructed from these points, with the stipulation that the sides of the rectangle must be parallel to the x and y axes. If it's impossible to form a rectangle with the provided points, the function should return 0.

The input `points` is a list of lists where each sublist contains two integers representing the x and y coordinates of a point. The constraints are 1 <= points.length <= 500, 0 <= points[i][0] <= 40000, and 0 <= points[i][1] <= 40000. All points are unique.
"""

def minAreaRect(points):
    from collections import defaultdict
    x_points = defaultdict(list) 
    min_area = float('inf') 
    for x, y in points:
        x_points[x].append(y)

    prev_x = {}
    for x in sorted(x_points):
        x_points[x].sort()
        for i in range(len(x_points[x])):
            for j in range(i):
                if (x_points[x][j], x_points[x][i]) in prev_x:
                    min_area = min(min_area, (x - prev_x[x_points[x][j], x_points[x][i]]) * (x_points[x][i] - x_points[x][j]))
                prev_x[x_points[x][j], x_points[x][i]] = x
    if min_area < float('inf'):
        return min_area
    return 0