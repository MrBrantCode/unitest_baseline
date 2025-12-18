"""
QUESTION:
Create a function `minPathWithBlockedCells` that takes a 2D grid `grid` of size NxN, an integer `k`, and a list of blocked cells `blockedCells` as input. The function should find the shortest route of length `k` in the grid while avoiding the blocked cells and following the grid's perimeter. Each cell in the grid has a unique numeric identifier from 1 to N*N. The function should return an ordered series of numeric identifiers representing the shortest route. If no such route exists, return -1. Note that each blocked cell in `blockedCells` is represented by a pair of its row and column indices (0-indexed).
"""

from queue import Queue
import sys

def minPathWithBlockedCells(grid, k, blockedCells):
    N = len(grid)
    distances = [[sys.maxsize for _ in range(N)] for _ in range(N)]
    
    # Mark blocked cells
    for blockedCell in blockedCells:
        distances[blockedCell[0]][blockedCell[1]] = -1

    # Start from each cell on the grid
    for i in range(N):
        for j in range(N):
            if distances[i][j] != -1:
                distances[i][j] = 0
                queue = Queue()
                queue.put((i, j))

                # Four possible directions
                directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

                # BFS
                while not queue.empty():
                    cur_i, cur_j = queue.get()
                    for direction in directions:
                        new_i, new_j = cur_i + direction[0], cur_j + direction[1]
                        # check if it's within the boundary of the grid and not blocked
                        if 0 <= new_i < N and 0 <= new_j < N and distances[new_i][new_j] != -1:
                            new_distance = distances[cur_i][cur_j] + 1
                            if new_distance < distances[new_i][new_j]:
                                distances[new_i][new_j] = new_distance
                                queue.put((new_i, new_j))

    # Return the cell values for the shortest path with length k
    path = []
    for i in range(N):
        for j in range(N):
            if distances[i][j] == k:
                path.append(grid[i][j])
    
    # If no path of length k is found, return -1
    if not path:
        return -1

    path.sort()
    return path