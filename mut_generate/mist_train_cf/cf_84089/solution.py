"""
QUESTION:
Write a function named `minCostConnectPoints` that takes two parameters: `points` and `obstacles`. `points` is a 2D list representing integer coordinates of some points on a 2D-plane, and `obstacles` is a 2D list representing the coordinates of obstacles. Return the minimum cost to make all points connected, where the cost of connecting two points is the Manhattan distance between them, doubled if the path crosses an obstacle. The points and obstacles arrays have lengths between 1 and 1000, and the coordinates are between -10^6 and 10^6.
"""

import heapq
import math

def calculate_cost(point1, point2, obstacles):
    """Calculate the cost of the edge between two points."""
    if (point1[0] == point2[0] or point1[1] == point2[1]) and (point1[0], point1[1]) not in obstacles and (point2[0], point2[1]) not in obstacles:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    else:
        return 2 * (abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]))

def minCostConnectPoints(points, obstacles):
    """Return the minimum cost to make all points connected."""
    n = len(points)
    graph = [[math.inf for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            cost = calculate_cost(points[i], points[j], obstacles)
            graph[i][j] = graph[j][i] = cost

    queue = [(0, 0)]
    visited = [False for _ in range(n)]
    total_cost = 0

    while queue:
        d, curr = heapq.heappop(queue)
        if not visited[curr]:
            visited[curr] = True
            total_cost += d

            for i in range(n):
                if visited[i]:
                    continue
                next_d = graph[curr][i]
                heapq.heappush(queue, (next_d, i))

    return total_cost