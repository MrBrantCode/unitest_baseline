"""
QUESTION:
Write a function named `find_islands` that takes a 2D matrix as input where 0's represent water and 1's represent land. The function should return the number of islands in the matrix, considering an island as a connected region of land that is not adjacent to the borders of the map, has a minimum area of 5 units, and has at least one unique feature.
"""

def find_islands(matrix):
    m = len(matrix)
    n = len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    count = 0
    
    def is_valid(i, j):
        return 0 <= i < m and 0 <= j < n and not visited[i][j] and matrix[i][j] == 1
    
    def dfs(i, j):
        visited[i][j] = True
        
        if matrix[i][j] == 1:
            matrix[i][j] = '*'  # marking the land as a unique feature
            
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = i + dx, j + dy
            if is_valid(nx, ny):
                dfs(nx, ny)
    
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if is_valid(i, j):
                dfs(i, j)
                count += 1
    
    return count