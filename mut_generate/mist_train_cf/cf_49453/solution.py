"""
QUESTION:
Find the longest diagonal sequence of unique integers in a given matrix. 

Implement a function `longest_unique_diagonal_sequence(matrix)` that takes as input a 2D matrix of integers and returns the length of the longest sequence of unique integers on any diagonal. The function should be able to handle matrices of any size and should be able to identify sequences that go from left to right (upwards or downwards) or from right to left (upwards or downwards).
"""

def longest_unique_diagonal_sequence(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_length = 0
    visited = [[False]*cols for _ in range(rows)]
    values = set()

    def dfs(i, j, length, diagonal_diff):
        nonlocal max_length
        if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j] or matrix[i][j] in values:
            return
        visited[i][j] = True
        values.add(matrix[i][j])
        max_length = max(max_length, length + 1)
        dfs(i + 1, j - 1, length + 1, diagonal_diff)
        dfs(i + 1, j + 1, length + 1, diagonal_diff)
        dfs(i - 1, j - 1, length + 1, diagonal_diff)
        dfs(i - 1, j + 1, length + 1, diagonal_diff)
        visited[i][j] = False
        values.remove(matrix[i][j])

    for k in range(rows + cols - 1):
        for i in range(rows):
            j = k - i
            if 0 <= j < cols:
                dfs(i, j, 0, k)

    return max_length