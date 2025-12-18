"""
QUESTION:
Create a function named `collect_treasures` that takes a 2D grid and three integers as input. The grid is represented as a list of lists of characters, where '.' represents an empty space, 'T' represents a treasure, and 'X' represents an obstacle. The three integers are the starting row, the starting column, and the maximum number of moves allowed. The function should return the maximum number of treasures that can be collected within the allowed number of moves without hitting any obstacles. The player can move up, down, left, or right within the grid.
"""

from typing import List

def collect_treasures(grid: List[List[str]], start_row: int, start_col: int, moves: int) -> int:
    def is_valid_move(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 'X'

    def collect_treasures_helper(row, col, moves_left):
        if moves_left < 0 or not is_valid_move(row, col):
            return 0
        if grid[row][col] == 'T':
            treasure_count = 1
        else:
            treasure_count = 0
        max_treasure_count = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            max_treasure_count = max(max_treasure_count, collect_treasures_helper(new_row, new_col, moves_left - 1))
        return treasure_count + max_treasure_count

    return collect_treasures_helper(start_row, start_col, moves)