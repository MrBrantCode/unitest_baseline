"""
QUESTION:
Write a function `count_islands(matrix)` that takes a 2D matrix of 0's and 1's as input, where 0's represent water and 1's represent land, and returns the number of islands formed by connecting adjacent lands horizontally or vertically. The function should not use any external libraries or classes, and it should not modify the input matrix.
"""

def count_islands(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] == 0 or visited[row][col]:
            return

        visited[row][col] = True

        dfs(row - 1, col)  # up
        dfs(row + 1, col)  # down
        dfs(row, col - 1)  # left
        dfs(row, col + 1)  # right

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count