"""
QUESTION:
Implement a function `find_shortest_path` that finds the shortest path from a given source point to a destination point in a 2D array while avoiding obstacles (represented by a value of 1). The function should return a list of coordinates representing the shortest path. If there is no valid path or the source/destination point is outside the array bounds or is an obstacle, return an empty list. The source and destination points are represented as [x, y] coordinates.
"""

from collections import deque

def find_shortest_path(array, source, destination):
    rows = len(array)
    cols = len(array[0])
    
    if (source[0] < 0 or source[0] >= rows or
        source[1] < 0 or source[1] >= cols or
        destination[0] < 0 or destination[0] >= rows or
        destination[1] < 0 or destination[1] >= cols):
        return []
    
    if array[source[0]][source[1]] == 1 or array[destination[0]][destination[1]] == 1:
        return []
    
    visited = [[False] * cols for _ in range(rows)]
    queue = deque()
    
    visited[source[0]][source[1]] = True
    queue.append((source[0], source[1], []))
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y, path = queue.popleft()
        
        if x == destination[0] and y == destination[1]:
            return path + [(x, y)]
        
        for dx, dy in moves:
            new_x = x + dx
            new_y = y + dy
            
            if (new_x >= 0 and new_x < rows and
                new_y >= 0 and new_y < cols and
                not visited[new_x][new_y] and
                array[new_x][new_y] != 1):
                
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, path + [(x, y)]))
    
    return []