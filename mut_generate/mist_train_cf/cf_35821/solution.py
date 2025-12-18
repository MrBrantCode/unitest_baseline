"""
QUESTION:
Implement the `play_game` function, which takes a 2D grid and a string of moves as input. The grid represents a world with empty spaces ('.'), treasures ('T'), obstacles ('X'), and the player's initial position ('P'). The function returns True if the player collects all treasures without encountering obstacles and False otherwise. The player can move up, down, left, or right within the grid boundaries, and the game ends when the player collects all treasures or encounters an obstacle.
"""

def play_game(grid, moves):
    rows, cols = len(grid), len(grid[0])
    treasures = sum(row.count('T') for row in grid)
    player_row, player_col = next((i, row.index('P')) for i, row in enumerate(grid) if 'P' in row)

    for move in moves:
        if move == 'U' and player_row > 0:
            player_row -= 1
        elif move == 'D' and player_row < rows - 1:
            player_row += 1
        elif move == 'L' and player_col > 0:
            player_col -= 1
        elif move == 'R' and player_col < cols - 1:
            player_col += 1

        if grid[player_row][player_col] == 'X':
            return False
        elif grid[player_row][player_col] == 'T':
            treasures -= 1
            grid[player_row][player_col] = '.'

    return treasures == 0