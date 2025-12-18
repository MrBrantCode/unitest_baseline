"""
QUESTION:
Create a function named `simulate_game` that takes three parameters: `grid`, `start_position`, and `goal_position`. The `grid` parameter is a string representing a 2D grid, with rows separated by commas and each cell either empty (denoted by '.') or containing an obstacle (denoted by 'X'). The `start_position` and `goal_position` parameters are strings representing the starting and goal positions in the format "row,col". The function should simulate a game where a player moves in four directions (up, down, left, and right) from the start position to the goal position, avoiding obstacles, and print the final state of the grid after the game simulation. If the player successfully reaches the goal, the goal position should be marked with 'G'. If the player hits an obstacle or goes out of bounds, the final position should be marked with 'P'.
"""

import sys

def simulate_game(grid, start_position, goal_position):
    rows = grid.split(',')
    grid_array = [list(row) for row in rows]
    start_row, start_col = map(int, start_position.split(','))
    goal_row, goal_col = map(int, goal_position.split(','))

    def is_valid_move(row, col):
        return 0 <= row < len(grid_array) and 0 <= col < len(grid_array[0]) and grid_array[row][col] != 'X'

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current_row, current_col = start_row, start_col

    for direction in directions:
        new_row, new_col = current_row + direction[0], current_col + direction[1]
        if is_valid_move(new_row, new_col):
            current_row, current_col = new_row, new_col

    if (current_row, current_col) == (goal_row, goal_col):
        grid_array[goal_row][goal_col] = 'G'
    else:
        grid_array[current_row][current_col] = 'P'

    for row in grid_array:
        print(''.join(row))