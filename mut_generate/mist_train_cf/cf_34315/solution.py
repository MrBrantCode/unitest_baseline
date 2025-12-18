"""
QUESTION:
Implement a function named `collect_treasures` that simulates a player collecting treasures in a grid-based game world. The function takes a 2D grid and a sequence of moves as input. The grid contains empty spaces ('.'), walls ('#'), and treasures ('T'). The sequence of moves consists of up ('U'), down ('D'), left ('L'), and right ('R') movements. The player starts at position (0, 0) and cannot move through walls. The function should return the total number of treasures collected by the player within the given sequence of moves. The grid is guaranteed to contain at least one empty space.
"""

from typing import List

def entrance(grid: List[List[str]], moves: List[str]) -> int:
    treasures_collected = 0
    x, y = 0, 0  

    for move in moves:
        if move == 'U' and x > 0 and grid[x - 1][y] != '#':
            x -= 1
        elif move == 'D' and x < len(grid) - 1 and grid[x + 1][y] != '#':
            x += 1
        elif move == 'L' and y > 0 and grid[x][y - 1] != '#':
            y -= 1
        elif move == 'R' and y < len(grid[0]) - 1 and grid[x][y + 1] != '#':
            y += 1

        if grid[x][y] == 'T':
            treasures_collected += 1
            grid[x][y] = '.'  

    return treasures_collected