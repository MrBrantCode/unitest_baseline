"""
QUESTION:
Write a function `count_islands(map)` that takes a 2D matrix as input where 0's represent water and 1's represent land. The function should return the number of islands in the map, where an island is defined as a connected region of land (horizontally, vertically, or diagonally) that is not adjacent to the borders of the map. The map is surrounded by water on all four sides.
"""

def count_islands(map):
    if not map or not map[0]:
        return 0

    rows = len(map)
    cols = len(map[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols and not visited[i][j] and map[i][j] == 1

    def dfs(i, j):
        visited[i][j] = True

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if is_valid(ni, nj):
                dfs(ni, nj)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if not visited[i][j] and map[i][j] == 1:
                dfs(i, j)
                count += 1

    return count