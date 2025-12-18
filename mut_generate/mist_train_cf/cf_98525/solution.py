"""
QUESTION:
Write a function `longest_path(maze, start, end)` that finds the length of the longest path between `start` and `end` points in a given `maze` without visiting any cell more than once. The `maze` is represented as a 2D array of integers, where 0 represents an empty cell and 1 represents a blocked cell. The `start` and `end` are the starting and ending cells of the path to be found, represented as tuples of row and column indices.
"""

def longest_path(maze, start, end):
    visited = set()
    max_path_length = 0
    
    def dfs(cell, path_length):
        nonlocal max_path_length
        max_path_length = max(max_path_length, path_length)
        visited.add(cell)
        for neighbor in get_unvisited_neighbors(maze, cell, visited):
            dfs(neighbor, path_length + 1)
        visited.remove(cell)
    
    def get_unvisited_neighbors(maze, cell, visited):
        row, col = cell
        neighbors = []
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nrow, ncol = row + drow, col + dcol
            if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[0]) and maze[nrow][ncol] != 1 and (nrow, ncol) not in visited:
                neighbors.append((nrow, ncol))
        return neighbors
    
    dfs(start, 1)
    return max_path_length