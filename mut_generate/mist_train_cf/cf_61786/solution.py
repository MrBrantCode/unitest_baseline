"""
QUESTION:
Write a function `shortest_path` that takes a 2D grid and an integer `k` as input, where the grid represents a matrix of 0s (empty spaces) and 1s (obstacles), and `k` is the maximum number of obstacles that can be eliminated. The function should return the minimum number of steps required to traverse from the top left corner to the bottom right corner, or -1 if it's impossible. The constraints are: `1 <= len(grid) == len(grid[0]) <= 40`, `1 <= k < len(grid) * len(grid[0])`, `grid[0][0] == grid[-1][-1] == 0`.
"""

import collections

def shortest_path(grid, k):
    m, n = len(grid), len(grid[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    deque = collections.deque([(0, 0, 0, k)]) 
    visited = {(0, 0): k}

    while deque:
        x, y, steps, remainingK = deque.popleft()

        if x == m-1 and y == n-1:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                nextK = remainingK - grid[nx][ny]
                if nextK >= 0 and (nx, ny) not in visited or nextK > visited.get((nx, ny), -1):
                    visited[(nx, ny)] = nextK
                    deque.append((nx, ny, steps+1, nextK))

    return -1