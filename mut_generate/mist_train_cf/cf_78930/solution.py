"""
QUESTION:
Implement a `GameOfLife` class with a method `step` that simulates one step of Conway's Game of Life with toroidal boundary conditions. The grid size is specified by the `size` parameter in the constructor. The grid is initialized with random values. 

The `step` method should apply the following rules:
- Any live cell with fewer than two live neighbours dies.
- Any live cell with two or three live neighbours survives.
- Any live cell with more than three live neighbours dies.
- Any dead cell with exactly three live neighbours becomes a live cell.

Note: The grid should wrap around to the opposite side at the edges, meaning that cells on the edge of the grid should consider cells on the opposite side as their neighbours.
"""

import numpy as np

def game_of_life_step(grid):
    """
    Simulates one step of Conway's Game of Life with toroidal boundary conditions.

    Parameters:
    grid (numpy array): The current state of the game grid.

    Returns:
    new_grid (numpy array): The state of the game grid after one step.
    """
    size = grid.shape[0]
    new_grid = np.copy(grid)
    for i in range(size):
        for j in range(size):
            count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    col = (j + y + size) % size
                    row = (i + x + size) % size
                    count += grid[row, col]
            count -= grid[i, j]
            if grid[i, j] == 1:
                if (count < 2) or (count > 3): 
                    new_grid[i, j] = 0
            elif grid[i, j] == 0:
                if count == 3:
                    new_grid[i, j] = 1
    return new_grid