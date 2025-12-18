"""
QUESTION:
Implement a `RoverRunner` class that simulates the movement of a rover on a rectangular grid. The grid is represented by a set of coordinates (x, y). The rover is controlled by a sequence of commands that represent movement and rotation instructions. 

The class should have an initializer method `__init__(self, grid, initial_position, initial_direction)` and a method `execute_commands(self, commands)` that executes the given sequence of commands to move and rotate the rover on the grid. 

The movement and rotation commands are 'L' (rotate 90 degrees to the left), 'R' (rotate 90 degrees to the right), and 'M' (move one grid point forward in the direction the rover is currently facing). The rover should ignore any further movement commands that would cause it to go out of bounds and any invalid commands.
"""

def execute_commands(commands, grid, initial_position, initial_direction):
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVEMENT = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    x, y = initial_position
    direction = initial_direction

    for command in commands:
        if command == 'L':
            current_index = DIRECTIONS.index(direction)
            direction = DIRECTIONS[(current_index - 1) % 4]
        elif command == 'R':
            current_index = DIRECTIONS.index(direction)
            direction = DIRECTIONS[(current_index + 1) % 4]
        elif command == 'M':
            dx, dy = MOVEMENT[direction]
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < grid[0] and 0 <= new_y < grid[1]:
                x, y = new_x, new_y
    return x, y, direction