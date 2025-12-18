"""
QUESTION:
You are given a set of unique coordinates in the xy-plane. Implement a function `minimum_area_rectangle(points)` to compute the smallest possible area of a rectangle that can be formed using these points, with the condition that the rectangle's sides must align with the x and y axes. If the given points do not allow the formation of a rectangle, the output should be 0. The input `points` is a list of lists, where each sublist contains two integers representing the x and y coordinates of a point. The constraints are: 1 <= len(points) <= 500, 0 <= points[i][0] <= 40000, 0 <= points[i][1] <= 40000, and all points are distinct.
"""

def minimum_area_rectangle(points):
    coordinates = set(map(tuple, points))
    n = len(points)
    min_area = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            if (p1[0], p2[1]) in coordinates and (p2[0], p1[1]) in coordinates:
                if p1[0] != p2[0] and p1[1] != p2[1]:
                    area = abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])
                    min_area = min(min_area, area)
    return min_area if min_area != float('inf') else 0