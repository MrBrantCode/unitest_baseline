"""
QUESTION:
Write a function called `canMouseWin` that determines if the mouse can reach the cat in a given grid. The mouse and cat can only move in the four main directions (up, down, left, right) and can jump a certain number of cells (mouse_jump and cat_jump) in a single step. The grid is represented as a 2D array where 'C' represents the cat, 'M' represents the mouse, 'F' represents food, 'H' represents holes, and '#' represents walls. The mouse can only win if it can reach the cat without being caught. The function should return True if the mouse can win, False otherwise. 

The function takes the following parameters: 
- grid: A 2D array representing the grid
- cat_jump: The number of cells the cat can jump in a single step
- mouse_jump: The number of cells the mouse can jump in a single step
"""

def canMouseWin(grid, catJump, mouseJump):
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    in_degrees = [[0] * n for _ in range(m)]

    # Initialize queue and in-degrees for mouse and cat
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'M':
                queue.append((i, j, 0, 1))  # (x, y, time, is_mouse)
            elif grid[i][j] == 'C':
                queue.append((i, j, 0, 0))  # (x, y, time, is_mouse)

    # BFS
    while queue:
        x, y, time, is_mouse = queue.pop(0)
        if is_mouse:
            if grid[x][y] == 'C':
                return True
            jump = mouseJump
        else:
            if grid[x][y] == 'M' or time > 0:
                continue
            jump = catJump

        for dx, dy in directions:
            nx, ny = x + dx * jump, y + dy * jump
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                if is_mouse:
                    if grid[nx][ny] == 'F':
                        continue
                    if in_degrees[nx][ny] == 0:
                        queue.append((nx, ny, time + 1, 1))
                        in_degrees[nx][ny] = 1
                else:
                    if in_degrees[nx][ny] == 0:
                        queue.append((nx, ny, time + 1, 0))
                        in_degrees[nx][ny] = 1

    return False