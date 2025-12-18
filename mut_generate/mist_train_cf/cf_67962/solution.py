"""
QUESTION:
Implement the `shortest_path` function, which uses the A* search algorithm to find the shortest path in a 2D array grid from a specified start point to a specified end point. The grid is represented as a 2D list of integers, where 1 represents an obstacle and 0 represents an open space. The start and end points are tuples of two integers representing their coordinates in the grid. The function should return the shortest path from the start point to the end point as a list of coordinates. If there is no path to the end point, the function should return None or an empty list.

The function should use a priority queue to keep track of the nodes to visit, and it should use a heuristic function to estimate the distance from each node to the end point. The heuristic function should be the Manhattan distance (also known as the L1 distance) between two points.

The function should also use a dictionary to keep track of the paths to each node, and it should use this dictionary to construct the shortest path once the end point is reached. 

The grid, start point, and end point will be valid inputs. The start and end points will be within the grid boundaries and will not be obstacles.
"""

import heapq

def shortest_path(grid, start, end):
    heap = [(0, start)]
    paths = {start: (None, 0)}
    while heap:
        (cost, current) = heapq.heappop(heap)
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = paths[current][0]
            return path[::-1]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:
                next_node = (x, y)
                new_cost = cost + 1
                if next_node not in paths or new_cost < paths[next_node][1]:
                    paths[next_node] = (current, new_cost)
                    heapq.heappush(heap, (new_cost + abs(x - end[0]) + abs(y - end[1]), next_node))
    return None