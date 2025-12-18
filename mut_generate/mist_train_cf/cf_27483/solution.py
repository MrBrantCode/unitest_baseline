"""
QUESTION:
Implement the `find_path()` function to solve a maze using the A* algorithm, where the maze is represented as a 2D grid with empty cells (0) and blocked cells (1). The function should return a list of tuples representing the coordinates of the cells in the shortest path from start to end, or an empty list if no path exists. 

You have access to the following functions from the `maze_map` module:
- `get_start()`: Returns the coordinates of the start cell as a tuple (x, y).
- `get_end()`: Returns the coordinates of the end cell as a tuple (x, y).
- `is_valid(x, y)`: Returns True if the cell at coordinates (x, y) is within the maze and is not blocked.
- `heuristic(x, y)`: Returns the Manhattan distance from cell (x, y) to the end cell.

Assume the maze has a valid start and end point, and there is at least one valid path from start to end.
"""

import heapq

def find_path(maze_map):
    start = maze_map.get_start()
    end = maze_map.get_end()
    
    open_set = [(0, start, [])]  # (f, (x, y), path)
    closed_set = set()
    
    while open_set:
        _, (x, y), path = heapq.heappop(open_set)
        
        if (x, y) == end:
            return path + [(x, y)]
        
        if (x, y) in closed_set:
            continue
        
        closed_set.add((x, y))
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if maze_map.is_valid(new_x, new_y):
                new_path = path + [(x, y)]
                g = len(new_path)
                h = maze_map.heuristic(new_x, new_y)
                f = g + h
                heapq.heappush(open_set, (f, (new_x, new_y), new_path))
    
    return []  # No path found