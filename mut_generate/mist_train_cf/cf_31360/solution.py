"""
QUESTION:
Implement a Python function `simulate_drone_movement` that simulates the movement of a drone in 3D space based on a list of movement commands. The function should take in an initial position as a tuple `(x, y, z)` and a list of movement commands, where each command is a tuple `(lr, fb, turning, ud)` representing left-right, front-back, turning, and up-down movement parameters. The function should update the drone's position based on each movement command and return its final position as a tuple. Assume the movement commands are applied sequentially in the order they appear in the list.
"""

def simulate_drone_movement(initial_position, movement_commands):
    current_position = list(initial_position)  
    for command in movement_commands:
        left_right, front_back, turning, up_down = command
        current_position[0] += left_right  
        current_position[1] += front_back  
        current_position[2] += up_down  
        # Turning is not considered in the 2D movement simulation

    return tuple(current_position)  