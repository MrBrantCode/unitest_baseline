"""
QUESTION:
Create a function `worldgen_path(grid)` that generates a continuous path through a given 2D grid without intersecting itself. The grid is a square (n x n) where n > 1, with each cell being either empty (0) or occupied (1). The function should return a list of coordinates representing the generated path, ensuring each step is adjacent to the previous step (horizontally, vertically, or diagonally). There will always be at least one valid path through the grid.
"""

def worldgen_path(grid):
    n = len(grid)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    def is_valid_move(x, y):
        return 0 <= x < n and 0 <= y < n and grid[x][y] == 0
    
    def find_path(x, y, visited):
        if (x, y) in visited or not is_valid_move(x, y):
            return None
        visited.add((x, y))
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            path = find_path(new_x, new_y, visited)
            if path is not None:
                return [(x, y)] + path
        return [(x, y)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                path = find_path(i, j, set())
                if path:
                    return path