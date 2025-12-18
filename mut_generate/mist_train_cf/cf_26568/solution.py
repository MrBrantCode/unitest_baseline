"""
QUESTION:
Write a function `line` that takes four integer arguments `x1`, `y1`, `x2`, and `y2`, representing the coordinates of two points (x1, y1) and (x2, y2) on a 2D plane. The function should return a list of tuples representing the points on the line between (x1, y1) and (x2, y2) using Bresenham's line algorithm. The function should handle cases where the line is horizontal, vertical, or diagonal, and it should handle both positive and negative slopes.
"""

from typing import List, Tuple

def line(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points