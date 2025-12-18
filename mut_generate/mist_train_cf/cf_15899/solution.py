"""
QUESTION:
Implement a function named `find_shortest_path` that takes a 2D list `matrix` and two points `start` and `end` as input, and returns the shortest path distance between the two points using Dijkstra's algorithm. The function should consider diagonal movement as a valid option and return -1 if there's no valid path between the start and end points. The matrix will contain non-negative integers representing the weights of the edges. The start and end points are represented as lists of two integers, e.g., [0, 0] and [2, 2].
"""

import heapq

def find_shortest_path(matrix, start, end):
    """
    This function finds the shortest path distance between two points in a 2D matrix using Dijkstra's algorithm.
    
    Args:
    matrix (list of lists): A 2D list representing the weights of the edges.
    start (list): A list of two integers representing the start point.
    end (list): A list of two integers representing the end point.
    
    Returns:
    int: The shortest path distance between the start and end points. Returns -1 if there's no valid path.
    """
    
    # Define the possible movements (up, down, left, right, and diagonals)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    # Initialize the distance to the start point as 0 and all other points as infinity
    dist = {(i, j): float('inf') for i in range(len(matrix)) for j in range(len(matrix[0]))}
    dist[tuple(start)] = 0
    
    # Initialize the priority queue with the start point
    pq = [(0, start)]
    
    while pq:
        # Get the point with the smallest distance from the priority queue
        current_dist, current = heapq.heappop(pq)
        
        # If the current point is the end point, return the distance
        if current == end:
            return current_dist
        
        # If the current distance is greater than the already known distance, skip this point
        if current_dist > dist[tuple(current)]:
            continue
        
        # Explore the neighbors of the current point
        for movement in movements:
            neighbor = (current[0] + movement[0], current[1] + movement[1])
            
            # Check if the neighbor is within the matrix boundaries
            if 0 <= neighbor[0] < len(matrix) and 0 <= neighbor[1] < len(matrix[0]):
                # Calculate the new distance to the neighbor
                new_dist = current_dist + matrix[neighbor[0]][neighbor[1]]
                
                # If the new distance is smaller than the already known distance, update it
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, list(neighbor)))
    
    # If there's no valid path to the end point, return -1
    return -1