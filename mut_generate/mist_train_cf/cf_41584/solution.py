"""
QUESTION:
Implement a function `calculate_manhattan_distance` that takes a list of navigation instructions and returns the Manhattan distance between the ship's starting position and its final position after executing all the instructions. The ship starts at the origin (0, 0) on a 2D grid and has a waypoint relative to its position at (10, 1). The navigation instructions consist of a sequence of actions and values, where each action represents a movement or rotation command for the ship and the waypoint. The actions are "N", "S", "E", "W", "L", "R", "F" with their respective effects: move the waypoint north, south, east, or west, rotate the waypoint around the ship's current position by 90 degrees in the specified direction, and move the ship to the waypoint a number of times equal to the given value. The function should return an integer representing the Manhattan distance between the ship's starting position and its final position.
"""

from typing import List

def calculate_manhattan_distance(instructions: List[str]) -> int:
    x, y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    ORDER = {
        "L": lambda x, y: (y, -x),
        "R": lambda x, y: (-y, x)
    }

    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action in ("N", "S", "E", "W"):
            if action == "N":
                waypoint_y += value
            elif action == "S":
                waypoint_y -= value
            elif action == "E":
                waypoint_x += value
            elif action == "W":
                waypoint_x -= value
        elif action in ("L", "R"):
            value = int(value/90) % 4
            for _ in range(value):
                waypoint_x, waypoint_y = ORDER[action](waypoint_x, waypoint_y)
        elif action == "F":
            x += value*waypoint_x
            y += value*waypoint_y
    return abs(x) + abs(y)