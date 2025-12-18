"""
QUESTION:
Implement a function `simulate_nomad` that takes three parameters: the size of a grid, the initial position of a player, and a sequence of movement commands. The function should update the player's position based on the movement commands and return the final position. The player can move in four directions (up, down, left, and right) within the grid boundaries. The movement commands are represented by 'U', 'D', 'L', and 'R', and any command that would cause the player to move outside the grid should be ignored. The final position should be returned in the format "(x, y)".
"""

def simulate_nomad(grid_size, initial_position, movement_commands):
    x, y = initial_position
    max_x, max_y = grid_size - 1, grid_size - 1

    for command in movement_commands:
        if command == 'U' and y < max_y:
            y += 1
        elif command == 'D' and y > 0:
            y -= 1
        elif command == 'L' and x > 0:
            x -= 1
        elif command == 'R' and x < max_x:
            x += 1

    return f"({x}, {y})"