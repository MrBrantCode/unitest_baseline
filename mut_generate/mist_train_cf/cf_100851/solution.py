"""
QUESTION:
The function `longest_path` should take a 2D array `maze` and two tuples `start` and `end` as input, where `maze` represents a maze with 0 as empty cells and 1 as blocked cells, and `start` and `end` are the starting and ending cells of the path. The function should return the length of the longest path between the `start` and `end` cells without visiting any cell more than once.
"""

def longest_path(maze, start, end):
    # initialize visited set and maximum path length
    visited = set()
    max_path_length = 0
    
    # helper function to explore the maze recursively
    def dfs(cell, path_length):
        nonlocal max_path_length
        # update the maximum path length found so far
        max_path_length = max(max_path_length, path_length)
        # add the current cell to the visited set
        visited.add(cell)
        # explore all unvisited neighbors recursively
        for neighbor in get_unvisited_neighbors(maze, cell, visited):
            dfs(neighbor, path_length + 1)
        # backtrack by removing the current cell from the visited set
        visited.remove(cell)
    
    # start exploring from the starting cell
    dfs(start, 1)
    # return the maximum path length found
    return max_path_length

def get_unvisited_neighbors(maze, cell, visited):
    # helper function to get unvisited neighbors of a cell
    row, col = cell
    neighbors = []
    for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nrow, ncol = row + drow, col + dcol
        if 0 <= nrow < len(maze) and 0 <= ncol < len(maze[0]) and maze[nrow][ncol] != 1 and (nrow, ncol) not in visited:
            neighbors.append((nrow, ncol))
    return neighbors