"""
QUESTION:
Implement a function `makePath` that takes a grid and an integer `l` as input. The function should use depth-first search to find the path of length `l` with the maximum sum of values in the grid. The path can move up, down, left, or right, but cannot visit the same cell twice. The function should return a list of values along the maximum path.
"""

def makePath(grid, l):
    M = len(grid)
    moves = [(-1,0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    maxPath, maxSum = [], 0
    
    def isValid(i, j, path):  # Check if a move is valid
        if i < 0 or j < 0 or i >= M or j >= M or (i, j) in path:
            return False
        return True

    def dfs(i, j, path):  # Depth-first search to find all paths
        nonlocal maxPath, maxSum
        if len(path) == l:  # If the path is of length `l`
            pathSum = sum(grid[x][y] for x, y in path)
            if pathSum > maxSum:
                maxPath, maxSum = path, pathSum
        else:
            for move in moves:
                ni, nj = i + move[0], j + move[1]
                if isValid(ni, nj, path):
                    dfs(ni, nj, path + [(ni, nj)])

    for i in range(M):
        for j in range(M):
            dfs(i, j, [(i, j)])

    return [grid[i][j] for i, j in maxPath]  # Return the values along the maximum path