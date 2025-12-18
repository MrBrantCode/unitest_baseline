"""
QUESTION:
Implement a function named `game_of_life` that takes two inputs: a 2D grid of integers and an integer `k`. The grid represents a game board with cells in one of three states: 0 (dead), 1 (alive), or 2 (has power). The function should simulate the game for `k` generations and return the final state of the grid.

The rules for each generation are as follows:
- A dead cell (0) becomes alive (1) if exactly 3 of its neighbors are alive, or if any of its neighbors have power.
- An alive cell (1) stays alive if 2 or 3 of its neighbors are alive, and dies otherwise.
- A cell with power (2) stays the same regardless of its neighbors.

The function should use a helper function `check` to count the number of alive neighbors and neighbors with power for each cell. The `check` function should take the grid and the coordinates of a cell as input, and return a tuple of two integers: the number of alive neighbors and the number of neighbors with power.
"""

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

def check(grid, r, c):
    live = 0
    power = 0
    for i in range(8):
        nr, nc = r + dx[i], c + dy[i]
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue
        if grid[nr][nc] == 1:
            live += 1
        elif grid[nr][nc] == 2:
            power += 1
    return live, power

def game_of_life(grid: list[list[int]], k: int) -> list[list[int]]:
    for _ in range(k):
        temp_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    temp_grid[i][j] = -1
                    continue

                live, power = check(grid, i, j)

                if grid[i][j] == 0 or grid[i][j] == 2:
                    if live == 3 or power:
                        temp_grid[i][j] = 1
                    else:
                        temp_grid[i][j] = 0
                else:
                    if live < 2 or live > 3:
                        temp_grid[i][j] = 0
                    else:
                        temp_grid[i][j] = 1
                if grid[i][j] == 2:
                    temp_grid[i][j] = 2

        grid = temp_grid
    return grid