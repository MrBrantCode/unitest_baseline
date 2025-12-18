"""
QUESTION:
Develop a function named `bfs` that takes a 2-dimensional array `maze` as input, representing a maze with 0s as walls and 1s as paths. The function should find the shortest path from the top-left corner (0,0) to the bottom-right corner and return the number of steps in the shortest path. The function should return `None` if no path exists. The maze is guaranteed to be a rectangle and the starting point is always at position (0,0) and the exit is always at the last cell of the array.
"""

from collections import deque

def bfs(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (rows-1, cols-1):
            return steps  # Found the exit

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, steps + 1))