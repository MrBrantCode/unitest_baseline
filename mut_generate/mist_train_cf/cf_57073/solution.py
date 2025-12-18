"""
QUESTION:
Write a function `hasPath(maze, start, destination)` that determines if a sphere can stop at a given destination within a labyrinth. The labyrinth is represented by a 2D array `maze` where 0 denotes a vacant space and 1 denotes a barrier. The sphere's start location is given by `start = [startrow, startcol]` and the destination is given by `destination = [destinationrow, destinationcol]`. The function should return True if the sphere can stop at the destination and False otherwise.

Constraints: 
- `m == len(maze)` and `n == len(maze[0])`
- `1 <= m, n <= 100`
- `labyrinth[i][j]` is either 0 or 1
- `start.length == 2` and `destination.length == 2`
- `0 <= startrow, destinationrow < m` and `0 <= startcol, destinationcol < n`
- The sphere and the destination are in vacant spaces and will not be in the same position initially.
- The labyrinth contains at least 2 vacant spaces.
"""

def hasPath(maze, start, destination):
    m, n, dest = len(maze), len(maze[0]), tuple(destination)
    start = tuple(start)
    visited = [[False]*n for _ in range(m)]

    def dfs(x, y):
        if (x, y) == dest:
            return True
        visited[x][y] = True
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x, y
            while 0 <= nx+dx < m and 0 <= ny+dy < n and maze[nx+dx][ny+dy] == 0:
                nx += dx
                ny += dy
            if not visited[nx][ny] and dfs(nx, ny):
                return True
        return False
    return dfs(start[0], start[1])