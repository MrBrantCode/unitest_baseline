"""
QUESTION:
Implement the function `simulate_roomba_movement(grid, initial_position, instructions)` that simulates a Roomba vacuum cleaner's movement in a room. The function takes a 2D grid representing the room where 0 represents a clean cell and 1 represents a dirty cell, the Roomba's initial position as a tuple (x, y), and a string of movement instructions ('U' for up, 'D' for down, 'L' for left, 'R' for right). The function should return the total number of cells cleaned by the Roomba after executing the given instructions. The Roomba's movement stops when it has executed all the instructions or when it tries to move outside the boundaries of the room.
"""

def simulate_roomba_movement(grid, initial_position, instructions):
    rows, cols = len(grid), len(grid[0])
    x, y = initial_position
    cleaned_cells = 0

    for move in instructions:
        if move == 'U' and x > 0:
            x -= 1
        elif move == 'D' and x < rows - 1:
            x += 1
        elif move == 'L' and y > 0:
            y -= 1
        elif move == 'R' and y < cols - 1:
            y += 1

        if grid[x][y] == 1:
            cleaned_cells += 1
            grid[x][y] = 0

    return cleaned_cells