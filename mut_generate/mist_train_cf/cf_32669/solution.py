"""
QUESTION:
Write a function `final_position(movements: List[str]) -> Tuple[int, int]` that takes a list of movement commands as input and returns the final position of the raccoon as a tuple of its coordinates (x, y) on the grid. The raccoon can move in four directions: up, down, left, and right, with each movement represented by a string in the format "go_up(n)", "go_down(n)", "go_left(n)", or "go_right(n)", where n is the number of units to move, defaulting to 1 if n is not specified. The grid is zero-indexed, and the top-left corner is (0, 0).
"""

from typing import List, Tuple

def entance(movements: List[str]) -> Tuple[int, int]:
    x, y = 0, 0  
    for movement in movements:
        if "go_up" in movement:
            steps = int(movement.split("(")[1].split(")")[0]) if "(" in movement else 1
            y += steps
        elif "go_down" in movement:
            steps = int(movement.split("(")[1].split(")")[0]) if "(" in movement else 1
            y -= steps
        elif "go_left" in movement:
            steps = int(movement.split("(")[1].split(")")[0]) if "(" in movement else 1
            x -= steps
        elif "go_right" in movement:
            steps = int(movement.split("(")[1].split(")")[0]) if "(" in movement else 1
            x += steps
    return x, y