"""
QUESTION:
Write a function `shortestPath` that takes a 2D array `arr` of size n x m as input, where `arr[i][j]` is 1 if the cell is open and 0 if it is blocked. The function should return the length of the shortest path from the top-left corner to the bottom-right corner, moving only through open cells in four directions: up, down, left, and right. If there is no path, return -1. The function signature should be `def shortestPath(arr: List[List[int]]) -> int`.
"""

from typing import List

def shortestPath(arr: List[List[int]]) -> int:
    n = len(arr)
    m = len(arr[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[0, 0]]
    visit = [[0] * m for _ in range(n)]
    visit[0][0] = 1

    while queue:
        y, x = queue.pop(0)
        if y == n - 1 and x == m - 1:
            return visit[y][x]
        for i in range(4):
            n_y = y + direction[i][0]
            n_x = x + direction[i][1]
            if 0 <= n_y < n and 0 <= n_x < m and arr[n_y][n_x] and not visit[n_y][n_x]:
                visit[n_y][n_x] = visit[y][x] + 1
                queue.append([n_y, n_x])

    return -1