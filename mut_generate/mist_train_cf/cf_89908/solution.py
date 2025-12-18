"""
QUESTION:
Write a function `shortest_path(grid, source, destination)` that finds the shortest path from a source point to a destination point in a given 2D array while avoiding obstacles (represented by a value of 1). The function should return a list of coordinates representing the shortest path, considering diagonal movement as valid. If there is no valid path, the function should return an empty list. The function should handle cases where the source point or destination point are outside the bounds of the array.
"""

from collections import deque

def shortest_path(grid, source, destination):
    rows = len(grid)
    cols = len(grid[0])

    # Check if source or destination are outside the bounds of the array
    if source[0] < 0 or source[0] >= rows or source[1] < 0 or source[1] >= cols:
        return []
    if destination[0] < 0 or destination[0] >= rows or destination[1] < 0 or destination[1] >= cols:
        return []

    # Check if source or destination are obstacles
    if grid[source[0]][source[1]] == 1 or grid[destination[0]][destination[1]] == 1:
        return []

    # Define possible directions for movement (including diagonals)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    # Initialize the visited array and the queue for BFS
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    queue.append((source[0], source[1], []))  # Each queue element contains (row, col, path)

    while queue:
        row, col, path = queue.popleft()

        # Check if we reached the destination point
        if row == destination[0] and col == destination[1]:
            return path + [(row, col)]

        # Check if the current cell is an obstacle or has already been visited
        if grid[row][col] == 1 or visited[row][col]:
            continue

        visited[row][col] = True

        # Add neighboring cells to the queue
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]

            # Check if the neighboring cell is within the array bounds
            if 0 <= new_row < rows and 0 <= new_col < cols:
                queue.append((new_row, new_col, path + [(row, col)]))

    # If no valid path was found
    return []