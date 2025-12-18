"""
QUESTION:
Implement a function `shortest_path` that takes a 2D array `grid` and two points `start` and `end` as input, and returns the shortest path distance from the `start` point to the `end` point using Dijkstra's algorithm. The grid represents a 2D array where each cell represents a node, and moving to an adjacent cell has a uniform cost of 1. The function should only consider moving up, down, left, or right.
"""

def shortest_path(grid, start, end):
    """
    This function calculates the shortest path distance from the start point to the end point using Dijkstra's algorithm.

    Args:
    grid (2D array): A 2D array representing the grid where each cell represents a node.
    start (tuple): The starting point coordinates.
    end (tuple): The ending point coordinates.

    Returns:
    int: The shortest path distance from the start point to the end point.
    """
    
    # Initialize the weights array with infinite values
    weights = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    weights[start[0]][start[1]] = 0
    
    # Define the possible directions (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Initialize the queue with the starting point
    q = [start]
    
    while q:
        # Dequeue the current cell
        curr = q.pop(0)
        
        # Get the current distance
        curr_dist = weights[curr[0]][curr[1]]
        
        # Explore all adjacent cells
        for direction in directions:
            row = curr[0] + direction[0]
            col = curr[1] + direction[1]
            
            # Check if the adjacent cell is within the grid
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                # Update the distance if a shorter path is found
                if weights[row][col] > curr_dist + 1:
                    weights[row][col] = curr_dist + 1
                    q.append((row, col))
                    
    # Return the shortest path distance
    return weights[end[0]][end[1]]