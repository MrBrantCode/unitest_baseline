"""
QUESTION:
Implement the function `simulate_robot_movement(grid, instructions)` that simulates the movement of a robot in a 2D grid environment. 

The function takes two parameters: 
- `grid`: a 2D list representing the grid environment where each cell is either 0 (empty) or 1 (obstacle).
- `instructions`: a string containing the movement instructions for the robot, where 'U' is up, 'D' is down, 'L' is left, and 'R' is right.

The function should return the final position of the robot as a tuple (x, y) after executing all the instructions, considering that the robot cannot move into cells occupied by obstacles or out of the grid. The robot starts at position (0, 0).
"""

def entance(grid, instructions):
    x, y = 0, 0  # Initial position of the robot
    n, m = len(grid), len(grid[0])  # Dimensions of the grid

    for move in instructions:
        if move == 'U' and x > 0 and grid[x - 1][y] == 0:
            x -= 1
        elif move == 'D' and x < n - 1 and grid[x + 1][y] == 0:
            x += 1
        elif move == 'L' and y > 0 and grid[x][y - 1] == 0:
            y -= 1
        elif move == 'R' and y < m - 1 and grid[x][y + 1] == 0:
            y += 1

    return x, y