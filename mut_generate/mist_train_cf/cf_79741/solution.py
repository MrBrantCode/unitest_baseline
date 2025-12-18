"""
QUESTION:
Write a function `shortest_path` that takes a 2D array `maze` filled with 0's and 1's (1 denotes an obstacle, 0 indicates free space) and two points `src` and `dest` as input. The function should return the shortest path from `src` to `dest` by only moving up, down, left, or right while avoiding obstacles. If no path exists, return -1. If multiple shortest paths exist, return any one.
"""

from collections import deque

def shortest_path(maze, src, dest):
    num_rows, num_cols = len(maze), len(maze[0]) 
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] 

    queue = deque([(src, 0)])
    visited = set()
    
    while queue:
        point, dist = queue.popleft()
        if point == dest:
            return dist
        for direction in directions:
            next_point = (point[0]+direction[0], point[1]+direction[1])
            if (0 <= next_point[0] < num_rows and 0 <= next_point[1] < num_cols and maze[next_point[0]][next_point[1]] == 0 and next_point not in visited):
                queue.append((next_point, dist+1))
                visited.add(next_point)

    return -1  # return -1 if no possible path