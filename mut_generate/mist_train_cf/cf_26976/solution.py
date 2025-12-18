"""
QUESTION:
Given a robot moving on a grid according to the rules: 
- move one step forward in the direction it is facing
- turn 90 degrees to the left
- move one step forward in the new direction, 
where the position update is done by `y += 1`, `y = y // 2`, `x = x // 2`, and the direction update is done by rotating 90 degrees to the left, 
write a function `final_position(steps: int, initial_position: Tuple[int, int]) -> Tuple[int, int]` that takes in the number of steps and the initial position (x, y), with the robot initially facing upwards (dy = -1), 
and returns the final position of the robot after taking the given number of steps.
"""

from typing import Tuple

def final_position(steps: int, initial_position: Tuple[int, int]) -> Tuple[int, int]:
    x, y = initial_position
    dx, dy = 0, -1

    for _ in range(steps):
        y += 1
        y = y // 2
        x = x // 2
        dx, dy = dy, -dx  # Rotate 90 degrees to the left

    return x, y