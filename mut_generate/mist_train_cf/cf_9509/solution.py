"""
QUESTION:
Implement a function called `find_shortest_path(matrix, start, end)` that uses Dijkstra's algorithm to find the shortest path between two points in a two-dimensional array. The function should take as input a 2D array `matrix`, a start point `start` represented as a tuple of two integers, and an end point `end` represented as a tuple of two integers. The function should return the length of the shortest path from the start point to the end point. If no path exists, the function should return -1.
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