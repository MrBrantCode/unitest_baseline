"""
QUESTION:
Implement a Python function `find_empty_positions(grid)` that takes a 2D grid as input where 0 represents an empty cell and 1 represents an occupied cell. The function should return a set containing all the empty positions (i, j) in the grid that are adjacent to at least one other empty cell. The function can use a helper function `n(pos)` that yields neighboring positions of a given position `pos` in the grid.
"""

def find_empty_positions(grid):
    def n(pos):
        i, j = pos
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                yield x, y

    empty = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                for neighbor in n((i, j)):
                    if grid[neighbor[0]][neighbor[1]] == 0 and neighbor != (i, j):
                        empty.add((i, j))
                        break
    return empty