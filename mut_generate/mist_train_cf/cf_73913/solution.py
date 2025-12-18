"""
QUESTION:
Given a list of commands where -2 represents a left turn, -1 represents a right turn, and 1-9 represent moving forward that many units, a list of obstacle coordinates, and the robot's battery life, implement a function called `robotSim` that returns the maximum Euclidean distance squared from the origin that the robot will be. The robot starts at the origin, faces north, and turns or moves based on the commands. If a move would take the robot to an obstacle or exceed the robot's remaining battery life, the move is aborted.
"""

def robotSim(commands, obstacles, battery):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    obstacles = set(map(tuple, obstacles))
    x = y = max_distance = direction_idx = 0

    for command in commands:
        if command == -2:  
            direction_idx = (direction_idx - 1) % 4  
        elif command == -1:  
            direction_idx = (direction_idx + 1) % 4
        else:  
            dx, dy = direction[direction_idx]
            while command > 0 and (x + dx, y + dy) not in obstacles and battery > 0:
                x += dx
                y += dy
                command -= 1
                battery -= 1 
            max_distance = max(max_distance, x**2 + y**2)
    return max_distance