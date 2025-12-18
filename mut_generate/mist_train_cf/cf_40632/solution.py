"""
QUESTION:
Write a function `final_position(moves: str) -> Tuple[int, int]` that takes a string `moves` of characters 'U', 'D', 'L', 'R', each representing up, down, left, right movements respectively, and returns a tuple of two integers representing the x-coordinate and y-coordinate of the final position of the robot after executing all the movements. The robot starts at (0, 0) facing up.
"""

from typing import Tuple

def final_position(moves: str) -> Tuple[int, int]:
    cur = [0, 0]

    for move in moves:
        if move == 'U':
            cur[1] += 1
        elif move == 'D':
            cur[1] -= 1
        elif move == 'L':
            cur[0] -= 1
        elif move == 'R':
            cur[0] += 1

    return tuple(cur)