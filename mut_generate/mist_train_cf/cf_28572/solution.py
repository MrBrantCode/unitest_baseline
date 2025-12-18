"""
QUESTION:
Implement a function `uniquePaths` that takes a 2D grid `maze` as input and returns the number of unique paths the player can take to reach the bottom-right corner from the top-left corner. The player can only move right or down, and cannot move diagonally. The grid contains '.' representing empty cells and '#' representing obstacles. The function should return 0 if the start or end cell is an obstacle.
"""

def uniquePaths(maze):
    rows, cols = len(maze), len(maze[0])
    
    # Create a 2D array to store the number of unique paths to reach each cell
    paths = [[0] * cols for _ in range(rows)]
    
    # Initialize the number of paths for the starting cell
    paths[0][0] = 1 if maze[0][0] == '.' else 0
    
    # Fill the first column with the number of paths to reach each cell
    for i in range(1, rows):
        if maze[i][0] == '.':
            paths[i][0] = paths[i-1][0]
    
    # Fill the first row with the number of paths to reach each cell
    for j in range(1, cols):
        if maze[0][j] == '.':
            paths[0][j] = paths[0][j-1]
    
    # Calculate the number of paths for each cell based on the paths from the adjacent cells
    for i in range(1, rows):
        for j in range(1, cols):
            if maze[i][j] == '.':
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
    
    return paths[rows-1][cols-1]