"""
QUESTION:
Implement the `is_square` function, which takes four lists of integers `p1`, `p2`, `p3`, and `p4` as input, representing the coordinates of four points in a 2D plane. Each list contains two integers representing the x and y coordinates of a point. The function should return `True` if the given points form a square with four equal sides and four right angles, and `False` otherwise.
"""

from typing import List

def is_square(p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    def distance(p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    distances = [distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3), distance(p2, p4), distance(p3, p4)]
    distances.sort()
    return 0 < distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]