"""
QUESTION:
Implement a function `minKnightMoves(x, y)` to find the minimum number of moves required for a knight to reach the square `[x, y]` from the starting position `[0, 0]` on an infinite chess board. The knight has 8 possible moves: two squares in a cardinal direction followed by one square in an orthogonal direction. The solution is guaranteed to exist, and the constraints are `|x| + |y| <= 300`.
"""

from collections import deque

def minKnightMoves(x, y):
    x, y = abs(x), abs(y)
    if x < y:
        x, y = y, x
    dq = deque([(0, 0, 0)])
    visited = set((0, 0))
    while dq:
        i, j, step = dq.popleft()
        if (i, j) == (x, y):
            return step
        for dx, dy in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]:
            ni, nj = i + dx, j + dy
            if -1 <= ni <= x + 2 and -1 <= nj <= y + 2 and (ni, nj) not in visited:
                visited.add((ni, nj))
                dq.append((ni, nj, step + 1))