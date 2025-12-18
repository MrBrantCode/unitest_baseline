"""
QUESTION:
Navigate the robot through the maze by executing a list of moves and return the final position of the robot. The maze is a 2D grid where 'R' denotes the robot's current position, '.' denotes empty cells, and '#' denotes walls. The moves are represented as strings containing 'U' for up, 'D' for down, 'L' for left, and 'R' for right. If the robot hits a wall, it should stop moving and remain at its current position. The function `navigate_maze(maze: List[str], moves: List[str]) -> str` should return the final position of the robot as a tuple of row and column indices.
"""

from typing import List

def navigate_maze(maze: List[str], moves: List[str]) -> str:
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    rows, cols = len(maze), len(maze[0])
    robot_pos = None

    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'R':
                robot_pos = (r, c)
                break

    if robot_pos is None:
        return "Robot not found in the maze"

    for move in moves:
        for m in move:
            dr, dc = directions[m]
            new_r, new_c = robot_pos[0] + dr, robot_pos[1] + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] != '#':
                robot_pos = (new_r, new_c)

    return robot_pos