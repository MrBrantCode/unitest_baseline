"""
QUESTION:
Implement a function called `gameOfLife` that takes a 2D grid `grid` and an integer `k` as input, where `grid` represents the initial state of an `m x n` board in the Game of Life with obstacles and power cells, and `k` represents the number of generations to simulate. The grid contains cells with the following states: live (1), dead (0), obstacle (-1), and power cell (2). The function should return the state of the grid after `k` generations, applying the rules of the Game of Life with obstacles and power cells simultaneously to every cell in each generation.

Restrictions: `m == grid.length`, `n == grid[i].length`, `1 <= m, n <= 50`, and `1 <= k <= 100`.
"""

def gameOfLife(grid: list[list[int]], k: int) -> list[list[int]]:
    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]

    def check(r, c):
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

    for _ in range(k):
        temp_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    temp_grid[i][j] = -1
                    continue

                live, power = check(i, j)

                if grid[i][j] == 0 or grid[i][j] == 2:
                    if live == 3:
                        temp_grid[i][j] = 1
                    elif power:
                        temp_grid[i][j] = 1
                    elif grid[i][j] == 2:
                        temp_grid[i][j] = 2
                else:
                    if live < 2 or live > 3:
                        temp_grid[i][j] = 0
                    else:
                        temp_grid[i][j] = 1

        grid = temp_grid
    return grid