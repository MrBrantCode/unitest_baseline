"""
QUESTION:
Implement a Python function `navigate_game` that simulates a game on a grid-based map. The function takes three parameters: a 2D list `grid_map` representing the game map, a tuple `start_position` representing the player's starting coordinates, and a string `movements` containing a sequence of movements ('U' for up, 'D' for down, 'L' for left, and 'R' for right). The function should return `True` if the player reaches the goal ('G') after following the movements, and `False` otherwise. The player cannot move into obstacles ('X').
"""

def navigate_game(grid_map, start_position, movements):
    x, y = start_position
    for move in movements:
        if move == 'U' and x > 0 and grid_map[x - 1][y] != 'X':
            x -= 1
        elif move == 'D' and x < len(grid_map) - 1 and grid_map[x + 1][y] != 'X':
            x += 1
        elif move == 'L' and y > 0 and grid_map[x][y - 1] != 'X':
            y -= 1
        elif move == 'R' and y < len(grid_map[0]) - 1 and grid_map[x][y + 1] != 'X':
            y += 1
        if grid_map[x][y] == 'G':
            return True
    return False