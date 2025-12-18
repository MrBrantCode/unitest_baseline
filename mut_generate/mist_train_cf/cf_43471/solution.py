"""
QUESTION:
Find the shortest path between two points in a matrix using a breadth-first search algorithm.

Given a matrix of size m x n, where each cell can either be traversable (value != 0) or an obstacle (value == 0), find the shortest path from a start point to an end point. The movement can be in eight directions: up, down, left, right, and four diagonals. The algorithm should return the path as a list of coordinates from the start point to the end point. If no path exists, return an empty list.

Restrictions: The algorithm should treat all traversable cells as equal, i.e., the actual matrix values do not affect the traversal cost. The start and end points are guaranteed to be valid coordinates within the matrix. The matrix does not contain any negative values.
"""

from collections import deque

def entrance(matrix, start, end):
    # These tuples are used to find the 8 possible movements from a cell
    possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Create a visited dictionary to mark cells as visited using cell coordinates as the key
    visited = {start: None}
    
    # Create a queue and enqueue the first node
    q = deque([start])
    
    # Until queue is not empty
    while q:
        node = q.popleft()
        
        # If destination is found, break
        if node == end:
            break
        
        # Check for all possible 8 movements from current cell
        for move in possible_movements:
            # Get the new cell coordinates
            x = node[0] + move[0]
            y = node[1] + move[1]
            next_node = (x, y)
            
            # Check if it is possible to go to new cell
            if (0 <= x < len(matrix)) and (0 <= y < len(matrix[0])) and (matrix[x][y] != 0) and (next_node not in visited):
                # Mark the cell as visited and enqueue it
                visited[next_node] = node
                q.append(next_node)
    
    # If we have reached the destination, we follow the path from destination to source
    path = []
    if end in visited:
        path.append(end)
        while path[-1] != start:
            path.append(visited[path[-1]])
        path.reverse()

    return path