"""
QUESTION:
Calculate the shortest distance between two points in a three-dimensional grid while avoiding obstacles. The grid represents a 3D space where each cell is a point. Some cells are impassable obstacles. Movement in the grid incurs different costs. Implement a function `calculate_shortest_distance` that takes as input the grid, the start point coordinates (x1, y1, z1), the target point coordinates (x2, y2, z2), and the movement costs, and returns the shortest distance between the start and target points while avoiding obstacles. The grid is represented as a 3D list of 0s (passable cells) and 1s (impassable cells). Movement costs are represented as a dictionary with the keys being the movement directions (e.g., 'up', 'down', 'left', 'right', 'forward', 'backward') and the values being the corresponding costs.
"""

from collections import deque
import heapq

def calculate_shortest_distance(grid, x1, y1, z1, x2, y2, z2, costs):
    """
    Calculate the shortest distance between two points in a three-dimensional grid while avoiding obstacles.
    
    Args:
    grid (3D list): A 3D list of 0s (passable cells) and 1s (impassable cells) representing the grid.
    x1, y1, z1 (int): The start point coordinates.
    x2, y2, z2 (int): The target point coordinates.
    costs (dict): A dictionary with movement directions as keys and costs as values.
    
    Returns:
    int: The shortest distance between the start and target points while avoiding obstacles.
    """
    
    # Define the possible movements in 3D space
    movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    
    # Initialize the queue for BFS, containing the start point and its cost
    queue = [(0, x1, y1, z1)]
    
    # Initialize a set to keep track of visited cells
    visited = set((x1, y1, z1))
    
    while queue:
        # Extract the cell with the minimum cost from the queue
        cost, x, y, z = heapq.heappop(queue)
        
        # If this is the target cell, return the cost
        if x == x2 and y == y2 and z == z2:
            return cost
        
        # Explore the neighbors of the current cell
        for dx, dy, dz in movements:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            # Check if the neighbor is within the grid boundaries and is not an obstacle
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and 0 <= nz < len(grid[0][0]) and
                    grid[nx][ny][nz] == 0 and (nx, ny, nz) not in visited):
                
                # Calculate the new cost based on the movement direction
                new_cost = cost + costs['up' if dz > 0 else 'down' if dz < 0 else 'right' if dy > 0 else 'left' if dy < 0 else 'forward' if dx > 0 else 'backward']
                
                # Mark the neighbor as visited and add it to the queue
                visited.add((nx, ny, nz))
                heapq.heappush(queue, (new_cost, nx, ny, nz))
    
    # If the target cell is not reachable, return -1
    return -1