"""
QUESTION:
Implement the function `calculate_shortest_distance` that takes in a 3D grid representing the environment and obstacles, and the coordinates of the starting and target points, and returns the shortest distance between the two points while avoiding the obstacles. The grid should be a 3D array where each cell contains a boolean indicating whether it's occupied by an obstacle and the height of the obstacle at that position. The coordinates should be tuples of three integers representing the x, y, and z coordinates. The function should return the shortest distance as a floating point number.
"""

import heapq

def calculate_shortest_distance(grid, start, target):
    """
    Calculate the shortest distance between two points in a 3D grid while avoiding obstacles.

    Args:
    grid (3D array): A 3D grid representing the environment and obstacles.
    start (tuple): The coordinates of the starting point.
    target (tuple): The coordinates of the target point.

    Returns:
    float: The shortest distance between the two points while avoiding the obstacles.
    """

    # Define the possible movements in 3D space
    movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    # Initialize the queue with the starting point
    queue = [(0, start)]
    visited = set([start])

    while queue:
        # Extract the point with the shortest distance from the queue
        (dist, current) = heapq.heappop(queue)

        # If the current point is the target, return the distance
        if current == target:
            return dist

        # Explore the neighbors of the current point
        for movement in movements:
            x, y, z = current[0] + movement[0], current[1] + movement[1], current[2] + movement[2]

            # Check if the neighbor is within the grid boundaries and not visited before
            if (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and (0 <= z < len(grid[0][0])) and (x, y, z) not in visited:
                # Check if the neighbor is not an obstacle
                if not grid[x][y][z][0]:
                    # Calculate the distance to the neighbor
                    neighbor_dist = dist + ((movement[0] ** 2 + movement[1] ** 2 + movement[2] ** 2) ** 0.5)

                    # Mark the neighbor as visited and add it to the queue
                    visited.add((x, y, z))
                    heapq.heappush(queue, (neighbor_dist, (x, y, z)))

    # If there's no path to the target, return infinity
    return float('inf')