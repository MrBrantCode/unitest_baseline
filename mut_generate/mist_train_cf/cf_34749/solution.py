"""
QUESTION:
Implement the `apply_rotations` function that takes a 2D grid of pixels and a list of rotation commands as input. Each pixel is initially set to either 0 or 1. The function should apply a series of column rotation commands to the grid and return the final state of the grid.

The grid is represented as a 2D list of integers where each element is either 0 or 1. The rotation commands are in the format "rotate column x=<column_index> by <steps>" where <column_index> is the index of the column to be rotated and <steps> is the number of steps to rotate the column. The rotation involves shifting the elements in the specified column downwards by the specified number of steps, with the bottom element wrapping around to the top.

The function should take two parameters: `grid` (a 2D list of integers) and `commands` (a list of strings representing the rotation commands). It should return the final state of the grid as a 2D list of integers.
"""

from typing import List

def apply_rotations(grid: List[List[int]], commands: List[str]) -> List[List[int]]:
    for command in commands:
        parts = command.split()
        col_index = int(parts[2].split('=')[1])
        steps = int(parts[-1])
        col = [grid[i][col_index] for i in range(len(grid))]
        col = col[-steps:] + col[:-steps]
        for i in range(len(grid)):
            grid[i][col_index] = col[i]
    return grid