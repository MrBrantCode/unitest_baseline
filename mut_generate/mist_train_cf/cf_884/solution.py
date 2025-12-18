"""
QUESTION:
Implement a function `find_shortest_path(matrix, start, end)` to find the shortest path between two points in a two-dimensional array using Dijkstra's algorithm. The function takes a 2D matrix of non-negative integers, a start point, and an end point as input. It should return the shortest distance from the start point to the end point. If there are no valid paths between the start and end points, the function should return -1. The algorithm should consider diagonal movement as a valid option when searching for the shortest path.
"""

import heapq

def find_shortest_path(matrix, start, end):
    """
    This function finds the shortest path between two points in a two-dimensional array using Dijkstra's algorithm.
    
    Args:
        matrix (list): A 2D matrix of non-negative integers.
        start (tuple): The start point.
        end (tuple): The end point.
    
    Returns:
        int: The shortest distance from the start point to the end point. Returns -1 if there are no valid paths.
    """

    # Define the possible movements (up, down, left, right, and diagonals)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Initialize the distance to the start point as 0, and all other points as infinity
    distances = {(i, j): float('inf') for i in range(len(matrix)) for j in range(len(matrix[0]))}
    distances[start] = 0

    # Initialize the priority queue with the start point
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the point with the smallest distance from the priority queue
        current_distance, current_point = heapq.heappop(priority_queue)

        # If the current point is the end point, return the distance
        if current_point == end:
            return current_distance

        # If the current distance is greater than the already found distance, skip this point
        if current_distance > distances[current_point]:
            continue

        # Explore the neighbors of the current point
        for movement in movements:
            new_i, new_j = current_point[0] + movement[0], current_point[1] + movement[1]

            # Check if the new point is within the matrix boundaries
            if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                # Calculate the new distance
                new_distance = current_distance + matrix[new_i][new_j]

                # If the new distance is smaller than the already found distance, update it
                if new_distance < distances[(new_i, new_j)]:
                    distances[(new_i, new_j)] = new_distance
                    # Add the new point to the priority queue
                    heapq.heappush(priority_queue, (new_distance, (new_i, new_j)))

    # If there are no valid paths, return -1
    return -1