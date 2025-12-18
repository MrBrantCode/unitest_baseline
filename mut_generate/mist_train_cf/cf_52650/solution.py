"""
QUESTION:
Given an `m x n` integers `matrix`, write a function `longestIncreasingPath` that returns the length of the longest increasing path in `matrix`. 

From each cell, you can move in four directions: left, right, up, or down. Some cells are marked as obstacles, represented by `-1` in the matrix, and cannot be moved into or through. 

Constraints: `m == matrix.length`, `n == matrix[i].length`, `1 <= m, n <= 200`, and `-1 <= matrix[i][j] <= 2^31 - 1`, where `-1` represents an obstacle.
"""

def longestIncreasingPath(matrix):
    if not matrix: 
        return 0
        
    memo = {} # Initialize memo dictionary
    directions = [(0,1), (0,-1), (1,0), (-1,0)] # Up, down, left, right
    max_length = 0 # Initialize max_length
        
    def dfs(i, j):
        # If the path length from (i, j) is already computed
        if (i, j) in memo: 
            return memo[(i, j)]
            
        # Otherwise, compute it by looking at all four possible directions
        length = 1
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j] and matrix[x][y] != -1:
                length = max(length, 1 + dfs(x, y))
                
        # Place the path length at memo[(i,j)] since it denotes the maximum length of increasing path from (i,j)
        memo[(i, j)] = length 
        return length

    # For each position in the matrix, check the longest path that can be formed
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != -1:
                max_length = max(max_length, dfs(i, j))
    return max_length