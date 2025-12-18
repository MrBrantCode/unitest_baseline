"""
QUESTION:
Implement a function `shortestPath(grid)` that takes a 2D grid representing a network of streets and returns the length of the shortest valid path from the top-left cell `(0,0)` to the bottom-right cell `(m - 1, n - 1)`. Each cell in the grid represents a street with a specific type (1-6) that connects to adjacent cells in certain directions. The function should return -1 if there is no valid path. The grid dimensions are m x n, where 1 <= m, n <= 300, and 1 <= grid[i][j] <= 6.
"""

def shortestPath(grid):
    """
    This function calculates the length of the shortest valid path from the top-left cell (0,0) 
    to the bottom-right cell (m - 1, n - 1) in a given grid.

    Args:
        grid (list of lists): A 2D grid representing a network of streets.

    Returns:
        int: The length of the shortest valid path, or -1 if there is no valid path.
    """

    # Define the BFS directions for each street
    directions = [
                    [],
                    [[0, -1], [0, 1]], 
                    [[-1, 0], [1, 0]],
                    [[0, -1], [1, 0]], 
                    [[0, 1], [1, 0]],
                    [[0, -1], [-1, 0]],
                    [[0, 1], [-1, 0]]
                ]

    # Get the dimensions of the grid
    m, n = len(grid), len(grid[0])

    # Initialize a grid to record the shortest distance to each cell
    distance = [[float('inf') for _ in range(n)] for _ in range(m)] 
    distance[0][0] = 0

    # Initialize a queue for BFS, starting from the top-left cell
    queue = [(0, 0)]

    # BFS traversal
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions[grid[x][y]]:
            nx, ny = x + dx, y + dy
            # Skip the cell if it's out of the grid or it's already visited
            if nx < 0 or nx >= m or ny < 0 or ny >= n or distance[nx][ny] <= distance[x][y] + 1:
                continue
            # Add the new cell to the queue
            queue.append((nx, ny))
            # Record the shortest distance to this cell
            distance[nx][ny] = distance[x][y] + 1

    # Return the shortest path length to the bottom-right cell, or -1 if it's not reachable
    return distance[m - 1][n - 1] if distance[m - 1][n - 1] < float('inf') else -1