"""
QUESTION:
Write a function `expand_maze(maze, fill)` that takes a 2D list `maze` of size `n x n` where `n` is an odd number and a fill character as input, and returns a new 2D list of size `2n x 2n` with the original maze positioned in the center, surrounded by a border of the fill character.
"""

def entrance(maze, fill):
    length = len(maze)
    expanded_length = length * 2
    expanded_maze = [[fill] * expanded_length for _ in range(expanded_length)]
    
    for i in range(length):
        for j in range(length):
            expanded_maze[i + length // 2][j + length // 2] = maze[i][j]
    
    return expanded_maze