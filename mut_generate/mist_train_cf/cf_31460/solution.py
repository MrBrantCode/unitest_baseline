"""
QUESTION:
Implement a function `panelMove` that takes a string of movement commands as input, where the commands are represented by the characters 'U' (up), 'D' (down), 'L' (left), and 'R' (right), and returns the final position of a panel on a 2D grid after executing the commands. The function should consider the grid boundaries and the initial position of the panel at (0, 0) on a 5x5 grid. The panel cannot move outside the grid boundaries.
"""

def panelMove(commands):
    initial_position = (0, 0)
    grid_width = 5
    grid_height = 5
    movements = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    
    current_position = initial_position
    
    for command in commands:
        movement_offset = movements.get(command, (0, 0))
        new_x = current_position[0] + movement_offset[0]
        new_y = current_position[1] + movement_offset[1]
        
        if 0 <= new_x < grid_width and 0 <= new_y < grid_height:
            current_position = (new_x, new_y)
    
    return current_position