"""
QUESTION:
Implement a function `navigateRobot(grid, start, end)` that takes in a 2D grid representing a grid environment where each cell is either empty (0) or blocked (1), a start position, and an end position. The function should return a list of movements ('up', 'down', 'left', 'right') for a robot to reach the end from the start, or an empty list if there's no valid path.
"""

def navigateRobot(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    movements = { (0, 1): 'right', (0, -1): 'left', (1, 0): 'down', (-1, 0): 'up' }

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0

    def backtrack_path(parents, start, end):
        path = []
        current = end
        while current != start:
            previous = parents[current]
            path.append(movements[(current[0] - previous[0], current[1] - previous[1])])
            current = previous
        return list(reversed(path))

    queue = [start]
    visited = set()
    parents = {}

    while queue:
        current = queue.pop(0)
        if current == end:
            return backtrack_path(parents, start, end)
        visited.add(current)
        for dr, dc in directions:
            new_row, new_col = current[0] + dr, current[1] + dc
            if (new_row, new_col) not in visited and is_valid_move(new_row, new_col):
                queue.append((new_row, new_col))
                parents[(new_row, new_col)] = current

    return []