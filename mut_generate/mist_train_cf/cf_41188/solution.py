"""
QUESTION:
Create a function `game_of_life` that takes two inputs: `initial_state` and `num_generations`. `initial_state` is a 2D list where 1 represents a live cell and 0 represents a dead cell. `num_generations` is an integer representing the number of generations to simulate.

The function should return a 2D list representing the state of the grid after simulating the specified number of generations, following these rules:
- Any live cell with fewer than two live neighbors dies.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies.
- Any dead cell with exactly three live neighbors becomes a live cell.
"""

def game_of_life(initial_state, num_generations):
    rows, cols = len(initial_state), len(initial_state[0])
    next_state = [[0] * cols for _ in range(rows)]

    def count_live_neighbors(row, col):
        count = 0
        for i in range(max(0, row - 1), min(rows, row + 2)):
            for j in range(max(0, col - 1), min(cols, col + 2)):
                count += initial_state[i][j]
        count -= initial_state[row][col]
        return count

    for _ in range(num_generations):
        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_live_neighbors(i, j)
                if initial_state[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        next_state[i][j] = 0
                    else:
                        next_state[i][j] = 1
                else:
                    if live_neighbors == 3:
                        next_state[i][j] = 1
                    else:
                        next_state[i][j] = 0
        initial_state = [row[:] for row in next_state]

    return next_state