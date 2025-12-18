"""
QUESTION:
Determine the minimum path consisting of k cells within an NxN grid where N >= 2. The grid cells contain unique values from 1 to N * N. Start from any cell and move to adjacent cells that share an edge. Return an ordered list of values along the minimum path, where the sum of the path values is minimized. Implement the function minPath(grid, k) to achieve this.
"""

def minPath(grid, k):
    n = len(grid)
    visited = [[False]*n for i in range(n)]

    def dfs(x, y, path):
        if len(path) == k:
            return path
        if x < 0 or y < 0 or x >= n or y >= n or visited[x][y]:
            return None
        visited[x][y] = True
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        min_path = None
        for dx, dy in directions:
            cur_path = dfs(x+dx, y+dy, path + [grid[x][y]])
            if cur_path is not None:
                if min_path is None or sum(cur_path) < sum(min_path):
                    min_path = cur_path
            visited[x][y] = False
        return min_path

    res = None
    for x in range(n):
        for y in range(n):
            path = dfs(x, y, [])
            if path is not None:
                if res is None or sum(path) < sum(res):
                    res = path
    return res