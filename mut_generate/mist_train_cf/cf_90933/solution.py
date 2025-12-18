"""
QUESTION:
Implement a function named `find_shortest_path` that takes a 2D matrix and two points, `start` and `end`, as input and returns the length of the shortest path between the `start` and `end` points in the matrix using Dijkstra's algorithm. The `start` and `end` points are tuples representing the coordinates in the matrix. The function should return -1 if no path exists between the `start` and `end` points.
"""

import heapq

def find_shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0

    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)

        if current == end:
            return dist

        if dist > distances[current[0]][current[1]]:
            continue

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current[0] + dx, current[1] + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                new_dist = dist + matrix[nx][ny]

                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, (nx, ny)))

    return -1  # No path found