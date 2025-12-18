"""
QUESTION:
Implement the `shortestPathAllKeys` function, which takes a 2D grid as input, where '.' is an unoccupied cell, '#' is a barrier, '@' is the initial position, ('a', 'b', ...) denote keys, and ('A', 'B', ...) are corresponding locks. The function should return the minimal number of moves required to collect all keys. If it's unachievable, return -1.

The input grid is a list of strings, where each string represents a row in the grid. The grid size is between 1x1 and 30x30. Each cell in the grid contains only '.', '#', '@', 'a'-'f', and 'A'-'F'. There are between 1 and 6 keys in the grid, each with a unique letter, and each key unlocks exactly one lock.
"""

from collections import deque

def shortestPathAllKeys(grid):
    m, n, numOfKeys = len(grid), len(grid[0]), 0
    x, y, keys, dp, d = 0, 0, 0, set(), deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                x, y = i, j
            if 'a' <= grid[i][j] <= 'f':
                numOfKeys += 1
    d.append((x, y, 0, 0))
    while d:
        x, y, keys, steps = d.popleft()
        if keys == (1 << numOfKeys) - 1: 
            return steps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                ch = grid[nx][ny]
                if ch == '#': 
                    continue
                elif 'A' <= ch <= 'F' and not (keys & (1 << (ord(ch) - ord('A')))): 
                    continue
                elif 'a' <= ch <= 'f':
                    keys |= (1 << (ord(ch) - ord('a')))
                if (nx, ny, keys) not in dp:
                    d.append((nx, ny, keys, steps + 1))
                    dp.add((nx, ny, keys))
    return -1