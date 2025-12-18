"""
QUESTION:
Implement the `play_game` function, which simulates a simple text-based game. The function takes two parameters: a 2D grid representing the game world and a string of player moves. The grid contains the following elements: '.' for empty space, 'T' for treasure, 'X' for obstacles, and 'P' for the player's initial position. The moves string contains 'U' for up, 'D' for down, 'L' for left, and 'R' for right.

The function should return a tuple `(collected_treasures, game_over)`, where `collected_treasures` is the number of treasures collected and `game_over` is a boolean indicating whether the game is over due to encountering an obstacle or not.

Assume the grid is rectangular and the player and treasures are initially placed in valid positions. If the player attempts to move outside the grid boundaries, the move is ignored.
"""

def play_game(grid, moves):
    rows, cols = len(grid), len(grid[0])
    player_row, player_col = -1, -1
    collected_treasures = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'P':
                player_row, player_col = r, c
                break

    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for move in moves:
        dr, dc = directions.get(move, (0, 0))
        new_row, new_col = player_row + dr, player_col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == 'T':
                collected_treasures += 1
            elif grid[new_row][new_col] == 'X':
                return collected_treasures, True  # Game over due to obstacle
            player_row, player_col = new_row, new_col

    return collected_treasures, False