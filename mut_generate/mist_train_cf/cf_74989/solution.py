"""
QUESTION:
Implement a function `shortestPathAllKeys` that takes a grid as input. The grid is a 2D list of characters where '@' represents the starting point, 'a' to 'f' represent keys, 'A' to 'F' represent locks that can be opened by the corresponding keys, and '#' represents a wall. The function should return the minimum number of steps to collect all keys and -1 if it's impossible.
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