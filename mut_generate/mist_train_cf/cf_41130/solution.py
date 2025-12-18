"""
QUESTION:
Create a function `simulateGame(grid, commands)` that simulates a simple text-based game. The game involves a character navigating through a grid-based world, collecting treasures, and avoiding obstacles. The function takes in a 2D array `grid` representing the game world and a string `commands` representing a sequence of movements. The function should return a string indicating the outcome of the game. 

The grid can contain the following characters: '.' for empty cells, 'X' for obstacles, 'S' for the character's initial position, and numbers from 1 to 9 for treasures. The character can move in four directions: up ('U'), down ('D'), left ('L'), and right ('R'). The function should return one of the following outcomes: "All treasures collected!" if all treasures are collected without encountering obstacles, "Game over, obstacle encountered!" if an obstacle is encountered before collecting all treasures, or "Game over, not all treasures collected!" if not all treasures are collected after completing the sequence of commands.
"""

def simulateGame(grid, commands):
    treasures = set(str(i) for i in range(1, 10))
    position = None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                position = (i, j)
                break

    for command in commands:
        if command == 'U':
            new_x, new_y = position[0] - 1, position[1]
        elif command == 'D':
            new_x, new_y = position[0] + 1, position[1]
        elif command == 'L':
            new_x, new_y = position[0], position[1] - 1
        elif command == 'R':
            new_x, new_y = position[0], position[1] + 1

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] in treasures:
                treasures.remove(grid[new_x][new_y])
                grid[new_x][new_y] = '.'
            elif grid[new_x][new_y] == 'X':
                return "Game over, obstacle encountered!"
            position = (new_x, new_y)
        else:
            return "Game over, out of bounds!"

    if not treasures:
        return "All treasures collected!"
    else:
        return "Game over, not all treasures collected!"