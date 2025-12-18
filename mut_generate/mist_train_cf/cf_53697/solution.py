"""
QUESTION:
Write a function `find_paths` that uses a recursive mechanism to find all unique paths through a given grid represented as a 2-D array. The grid contains "L" for land and "W" for water. The path starts from the top-left corner and ends at the bottom-right corner, with each step being either down or right. 

The function should also ensure the entered grid is a square and only contains the characters "L" or "W". 

Additionally, display the number of unique paths that avoid water ("W") cells. 

Note: The grid is 0-indexed, where the top-left corner is (0,0) and the bottom-right corner is (n-1, n-1) for an n x n grid. The "right" move is represented by 'R' and the "down" move is represented by 'D'.
"""

def find_paths(grid, x=0, y=0, path=''):
    """
    This function uses a recursive mechanism to find all unique paths through a given grid.
    
    Args:
    grid (list): A 2D list representing the grid, where "L" denotes land and "W" denotes water.
    x (int): The current x-coordinate (default is 0).
    y (int): The current y-coordinate (default is 0).
    path (str): The current path taken so far (default is an empty string).
    
    Returns:
    list: A list of all unique paths from the top-left corner to the bottom-right corner.
    """
    if not is_valid_grid(grid):
        return []
    
    if x == len(grid) - 1 and y == len(grid[0]) - 1 and grid[y][x] == "L":
        return [path]
    paths = []
    if x < len(grid) - 1 and grid[y][x+1] == "L":
        paths.extend(find_paths(grid, x=x+1, y=y, path=path+'R'))
    if y < len(grid) - 1 and grid[y+1][x] == "L":
        paths.extend(find_paths(grid, x=x, y=y+1, path=path+'D'))
    return paths

def is_valid_grid(grid):
    # check the grid is a square
    if len(grid) != len(grid[0]):
        return False
    # check the grid only contains "L" or "W"
    for row in grid:
        if not all(cell in ["L", "W"] for cell in row):
            return False
    return True