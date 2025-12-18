"""
QUESTION:
Implement the `play_game` function, which takes a 2D grid, a starting position, and a sequence of moves as input. The grid represents a game world where 0 is an empty cell, 1 is a cell containing a treasure, and -1 is a cell blocked by an obstacle. The function should return the total number of treasures collected by the player after making the specified sequence of moves. The player can move up, down, left, or right within the grid but cannot move through obstacles or outside the grid boundaries. The player starts at the given position with an initial treasure count of 0. If the player encounters an obstacle or moves out of the grid boundaries, the function should stop and return the total number of treasures collected up to that point.
"""

def play_game(grid, start, moves):
    rows, cols = len(grid), len(grid[0])
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    treasures_collected = 0
    current_position = start

    for move in moves:
        new_row = current_position[0] + directions[move][0]
        new_col = current_position[1] + directions[move][1]

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != -1:
            current_position = (new_row, new_col)
            if grid[new_row][new_col] == 1:
                treasures_collected += 1
        else:
            break

    return treasures_collected