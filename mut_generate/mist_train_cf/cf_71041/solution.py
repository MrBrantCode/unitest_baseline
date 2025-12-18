"""
QUESTION:
Implement a function `minimumMoves(grid)` that calculates the minimum number of moves a snake needs to reach the target position in a grid.

The snake starts at the top left corner and spans two cells. The grid is `n*n` in size, where `n` is between 2 and 100. The grid contains empty cells (0), blocked cells (1), and obstacle cells (2). The snake can move right, down, rotate clockwise, or rotate counterclockwise. Removing an obstacle costs 2 moves. The snake can be in two states: horizontal or vertical.

The function should return the minimum number of moves to reach the target position. If there is no way to reach the target, return -1.
"""

from collections import deque 

def minimumMoves(grid):
    n = len(grid)
    visited = [[[0, 0] for _ in range(n)] for _ in range(n)]
    q = deque([[(0, 0, 0, 1), 0, 0]])
    visited[0][0], visited[0][1] = [1, 1], [1,1]
    while q:
        pos, state, steps = q.popleft()
        x1, y1, x2, y2 = pos
        if (x1, y1) == (n-1, n-2) and (x2, y2) == (n-1, n-1):
            return steps
        for (dx, dy) in [(0, 1), (1, 0)]:
            nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
            if 0 <= nx1 < n and 0 <= nx2 < n and 0 <= ny1 < n and 0 <= ny2 < n:
                if (grid[nx1][ny1] <= 1 and grid[nx2][ny2] <= 1 ) and visited[nx1][ny1][state] == 0:
                    q.append([(nx1, ny1, nx2, ny2), state, steps+1])
                    visited[nx1][ny1][state] = 1
        for i in range(2):
            nx2, ny2, nstate = (x1 + dx, y1, 1 - state) if state == 0 else (x2, y2 + dy, 1 - state)
            if 0 <= nx2 < n and 0 <= ny2 < n and grid[nx2][ny2] <= 1 and visited[nx2][ny2][nstate] == 0:
                q.append([(x1, y1, nx2, ny2), nstate, steps+1])
                visited[nx2][ny2][nstate] = 1
    return -1