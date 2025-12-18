"""
QUESTION:
Write a function `finalPosition(commands: str) -> Tuple[int, int]` that takes a string `commands` containing a series of commands ('U', 'D', 'L', 'R') and returns a tuple representing the final position of a robot on a 2D grid after executing all the commands. The robot starts at position (0, 0) and can move up, down, left, or right. Ignore any other characters in the string.
"""

from typing import Tuple

def entance(commands: str) -> Tuple[int, int]:
    x, y = 0, 0  
    for command in commands:
        if command == 'U':
            y += 1
        elif command == 'D':
            y -= 1
        elif command == 'L':
            x -= 1
        elif command == 'R':
            x += 1
    return x, y