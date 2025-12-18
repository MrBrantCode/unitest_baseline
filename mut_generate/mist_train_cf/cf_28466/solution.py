"""
QUESTION:
Create a function `final_position` that takes a string of commands as input, where each character represents a direction the robot should move (N for north, S for south, E for east, W for west). The function should return the final position of the robot as a tuple of two integers representing the x and y coordinates, assuming the robot starts at (0, 0).
"""

from typing import Tuple

def final_position(commands: str) -> Tuple[int, int]:
    x, y = 0, 0
    for command in commands:
        if command == "N":
            y += 1
        elif command == "S":
            y -= 1
        elif command == "E":
            x += 1
        elif command == "W":
            x -= 1
    return x, y