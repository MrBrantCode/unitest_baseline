"""
QUESTION:
Write a function `count_groups` that takes a 2D array of elements as input, where each element represents a color. The function should count the number of groups of contiguous elements with the same color, with a minimum group size of 100 elements. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def count_groups(array):
    rows, cols = len(array), len(array[0])
    count = 0

    def dfs(i, j, color):
        nonlocal group_size
        if i < 0 or i >= rows or j < 0 or j >= cols or array[i][j] != color or visited[i][j]:
            return
        visited[i][j] = True
        group_size += 1
        if group_size == min_group_size:
            return
        dfs(i + 1, j, color)
        dfs(i - 1, j, color)
        dfs(i, j + 1, color)
        dfs(i, j - 1, color)

    visited = [[False] * cols for _ in range(rows)]
    min_group_size = 100

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                group_size = 0
                dfs(i, j, array[i][j])
                if group_size >= min_group_size:
                    count += 1

    return count