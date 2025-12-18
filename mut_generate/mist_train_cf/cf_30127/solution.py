"""
QUESTION:
Given a list of instructions in the form of tuples, where each tuple contains a string ("forward", "up", or "down") and an integer representing the distance to move, calculate the product of the final horizontal position and the final depth position after executing all the instructions.

The starting position is at the origin (0, 0, 0) in 3D space, and the "forward" instruction moves the position along the horizontal axis, the "up" instruction moves the position upwards, and the "down" instruction moves the position downwards.

Write a function `calculate_position_product(instructions: List[Tuple[str, int]]) -> int` to solve this problem.
"""

from typing import List, Tuple

def entrance(instructions: List[Tuple[str, int]]) -> int:
    hor_axis: int = 0
    depth: int = 0

    for instruction in instructions:
        match instruction[0]:
            case "forward":
                hor_axis += instruction[1]
            case "up":
                depth -= instruction[1]
            case "down":
                depth += instruction[1]

    return hor_axis * depth