"""
QUESTION:
Implement a function `find_shortest_path` that takes as input a 2D matrix of non-negative integers, a start point, and an end point. The function should return the shortest path distance from the start point to the end point using Dijkstra's algorithm, considering diagonal movement as a valid option. If there is no valid path between the start and end points, return -1.
"""

import heapq

def find_shortest_path(matrix, start, end):
    """
    This function implements Dijkstra's algorithm to find the shortest path 
    between a start point and an end point in a given 2D matrix. The function 
    considers diagonal movement as a valid option and returns -1 if there is no 
    valid path between the start and end points.

    Args:
        matrix (list): A 2D list of non-negative integers.
        start (list): The start point coordinates in the matrix.
        end (list): The end point coordinates in the matrix.

    Returns:
        int: The shortest path distance from the start point to the end point.
    """

    # Define the possible movements (up, down, left, right, and diagonals)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # Initialize the distance and priority queue
    dist = {(i, j): float('inf') for i in range(len(matrix)) for j in range(len(matrix[0]))}
    dist[tuple(start)] = 0
    pq = [(0, start)]

    # Perform Dijkstra's algorithm
    while pq:
        current_dist, current = heapq.heappop(pq)

        # If the current point is the end point, return the distance
        if current == end:
            return current_dist

        # Explore the neighbors of the current point
        for movement in movements:
            new_i, new_j = current[0] + movement[0], current[1] + movement[1]

            # Check if the new point is within the matrix boundaries
            if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                # Calculate the new distance
                new_distance = current_dist + matrix[new_i][new_j]

                # Update the distance if a shorter path is found
                if new_distance < dist[(new_i, new_j)]:
                    dist[(new_i, new_j)] = new_distance
                    heapq.heappush(pq, (new_distance, (new_i, new_j)))

    # If there is no valid path, return -1
    return -1