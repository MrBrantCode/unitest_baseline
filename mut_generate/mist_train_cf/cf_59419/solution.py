"""
QUESTION:
Design a function `rapidFoxSimulation(m, n, t, startX, startY, obstacles)` that simulates the movement of a rapid umber vulpine in a two-dimensional grid environment. The function should determine all the cells that the fox could possibly occupy after `t` time steps from a starting position `(startX, startY)` in a grid of dimensions `m x n` with given obstacles. 

The function should validate the inputs, ensuring that `m` and `n` are non-negative, `t` is non-negative, the starting position is within the grid and not an obstacle, and all obstacle coordinates are within the grid. The function should also optimize time and space complexity.
"""

from queue import Queue

def rapidFoxSimulation(m, n, t, startX, startY, obstacles):
    # Validate the inputs
    if m <= 0 or n <= 0 or t < 0:
        return "Invalid grid dimensions or time step"

    if startX < 0 or startX >= m or startY < 0 or startY >= n:
        return "Invalid starting position"

    for x, y in obstacles:
        if x < 0 or x >= m or y < 0 or y >= n:
            return "Invalid obstacles"

    if (startX, startY) in obstacles:
        return "Starting position can't be an obstacle"

    # Create grid and fill with obstacles
    grid = [[0]*n for _ in range(m)]
    for x, y in obstacles:
        grid[x][y] = -1

    # Define directions (north, south, east, west)
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = Queue()
    queue.put((startX, startY))

    # Mark the start cell as reachable in 0 steps
    grid[startX][startY] = t + 1

    while not queue.empty():
        x, y = queue.get()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] < grid[x][y] - 1:
                grid[nx][ny] = grid[x][y] - 1
                queue.put((nx, ny))

    # Gather all cells the fox can reach
    reachable_cells = [(i, j) for i in range(m) for j in range(n) if grid[i][j] > 0]

    return reachable_cells