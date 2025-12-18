"""
QUESTION:
Write a function `calculate_final_position` that takes a list of movement instructions as input, where each instruction is a string containing a direction (up, down, left, or forward) and a distance to move in that direction. The function should return the final position of the robot as a tuple of coordinates (x, y) after executing all the instructions, assuming the robot starts at the origin (0, 0) and moving up increases the x-coordinate, moving down decreases the x-coordinate, moving left decreases the y-coordinate, and moving forward increases the y-coordinate.
"""

def calculate_final_position(instructions):
    x, y = 0, 0
    for instruction in instructions:
        direction, distance = instruction.split()
        distance = int(distance)
        if direction == "forward":
            y += distance
        elif direction == "down":
            y -= distance
        elif direction == "left":
            x -= distance
        elif direction == "up":
            x += distance
    return (x, y)