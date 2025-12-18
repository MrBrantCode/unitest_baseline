"""
QUESTION:
Create a function `shortest_path` that finds the shortest path from a starting point `start` to a goal point `goal` in a given 2D list `matrix`. The function should assume that only four directions (up, down, left, and right) are allowed, and that the start and end points are represented as a tuple of coordinates in the format of `(x, y)`. The matrix contains `0`s representing blocked cells and non-zero cells that can be travelled on.
"""

from collections import deque
def shortest_path(matrix, start, goal):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x, y) == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(matrix[0]) and 0 <= y2 < len(matrix) and matrix[y2][x2] != 0 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))