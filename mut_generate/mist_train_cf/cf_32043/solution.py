"""
QUESTION:
Write a function `largest_rectangle_area` that takes a list of points in the 2D plane, each represented by a pair of integers (x, y), and returns the area of the largest rectangle that can be formed from these points with sides parallel to the x and y axes. If no rectangle can be formed, the function should return 0.
"""

from typing import List, Tuple

def largest_rectangle_area(points: List[Tuple[int, int]]) -> int:
    max_area = 0
    point_set = set(points)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                if (points[i][0], points[j][1]) in point_set and (points[j][0], points[i][1]) in point_set:
                    area = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1])
                    max_area = max(max_area, area)
    return max_area