"""
QUESTION:
Given a 2D array where each element represents a color, write a function named `count_groups` that takes this array as input and returns the number of groups of adjacent elements that have the same color. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def count_groups(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])
    visited = [[False] * n_cols for _ in range(n_rows)]
    group_count = 0

    def dfs(i, j, color):
        if i < 0 or i >= n_rows or j < 0 or j >= n_cols:
            return
        if visited[i][j] or matrix[i][j] != color:
            return
        visited[i][j] = True
        dfs(i+1, j, color)
        dfs(i-1, j, color)
        dfs(i, j+1, color)
        dfs(i, j-1, color)

    for i in range(n_rows):
        for j in range(n_cols):
            if not visited[i][j]:
                group_count += 1
                dfs(i, j, matrix[i][j])

    return group_count