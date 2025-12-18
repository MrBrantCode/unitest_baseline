"""
QUESTION:
Given an 8x8 grid representing a chessboard where "." denotes an empty cell and "Q" denotes a queen, write a function `count_attacked_cells` that takes the row and column indices of a queen as input and returns the count of empty cells that the queen can attack in the horizontal, vertical, and diagonal directions. The function should only consider cells within the grid boundaries and stop counting when a queen is encountered in a given direction.
"""

from typing import List

def entrance(board: List[List[str]], r_ind: int, c_ind: int) -> int:
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dr, dc in directions:
        cur_r, cur_c = r_ind, c_ind
        while 0 <= cur_r + dr < 8 and 0 <= cur_c + dc < 8:
            cur_r += dr
            cur_c += dc
            if board[cur_r][cur_c] == "Q":
                break
            count += 1

    return count