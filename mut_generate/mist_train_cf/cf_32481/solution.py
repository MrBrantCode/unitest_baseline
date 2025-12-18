"""
QUESTION:
Write a function `game_of_life` that takes a 2D list `board` of booleans as input and modifies it in-place to represent the next state of Conway's Game of Life. The function should follow these rules:
- Any live cell with fewer than two live neighbors dies.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies.
- Any dead cell with exactly three live neighbors becomes a live cell.

The input `board` is a 2D list of booleans where each element `board[i][j]` represents the state of the cell at position (i, j), with `True` indicating an alive cell and `False` indicating a dead cell. The function should not return any value.
"""

from typing import List

def game_of_life(board: List[List[bool]]) -> None:
    rows, cols = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def count_live_neighbors(row, col):
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and board[r][c]:
                count += 1
        return count

    next_state = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(r, c)
            if board[r][c]:  # current cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    next_state[r][c] = False  # cell dies
                else:
                    next_state[r][c] = True  # cell lives on
            else:  # current cell is dead
                if live_neighbors == 3:
                    next_state[r][c] = True  # cell becomes alive

    for r in range(rows):
        for c in range(cols):
            board[r][c] = next_state[r][c]