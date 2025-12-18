"""
QUESTION:
Write a function `isRobotBounded(instructions)` that determines if a robot remains bounded in a circle when given a sequence of instructions. The robot starts at `(0, 0)` and faces north. It can receive four instructions: `"G"` to go straight, `"L"` to turn 90 degrees left, `"R"` to turn 90 degrees right, and `"O"` to place an obstacle at the current position. If the robot encounters an obstacle, it stops moving and turns right. The function should return `True` if the robot remains bounded and `False` otherwise.

The function should assume that `instructions` is a string of length between 1 and 1000, consisting of only the characters `"G"`, `"L"`, `"R"`, and `"O"`.
"""

def isRobotBounded(instructions: str) -> bool:
    # north = 0, east = 1, south = 2, west = 3
    x, y, direction, path = 0, 0, 0, set()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for _ in range(4):
        for i in instructions:
            if i == 'R':
                direction = (direction + 1) % 4
            elif i == 'L':
                direction = (direction - 1) % 4
            elif i == 'O':
                path.add((x, y))
            elif (x + dx[direction], y + dy[direction]) not in path:
                x += dx[direction]
                y += dy[direction]
        if (x, y) == (0, 0):
            return True
    return False