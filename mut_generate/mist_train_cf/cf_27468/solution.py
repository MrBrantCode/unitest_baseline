"""
QUESTION:
Create a function `find_path` that finds a path from the start cell 'S' to the end cell 'E' in a given 2D maze grid. The maze grid is represented as a list of lists of characters, where '.' denotes an empty cell and '#' denotes a blocked cell. The start cell 'S' and end cell 'E' are guaranteed to be present in the maze, and there is a single possible path from 'S' to 'E'. The function should return the path as a sequence of movements: 'U' for up, 'D' for down, 'L' for left, and 'R' for right. If there is no valid path from 'S' to 'E', the function should return "No path found".
"""

def find_path(maze):
    """
    Finds a path from the start cell 'S' to the end cell 'E' in a given 2D maze grid.

    Args:
    maze (list of lists of characters): A 2D maze grid where '.' denotes an empty cell, '#' denotes a blocked cell, 'S' denotes the start cell, and 'E' denotes the end cell.

    Returns:
    str: The path as a sequence of movements: 'U' for up, 'D' for down, 'L' for left, and 'R' for right. If there is no valid path from 'S' to 'E', returns "No path found".
    """
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
                break
    
    queue = [(start, "")]
    visited = set()
    
    while queue:
        (x, y), path = queue.pop(0)
        if maze[x][y] == 'E':
            return path
        for direction, (dx, dy) in directions.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), path + direction))
                visited.add((new_x, new_y))
    return "No path found"