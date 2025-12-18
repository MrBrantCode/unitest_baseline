"""
QUESTION:
Implement a function `move_player` that moves the player within a given maze, considering the maze boundaries and obstacles. The maze is represented as a 2D grid, where each cell contains a symbol denoting the terrain or obstacle. The function should take two parameters: the maze and the direction of movement. The player's position is initially at [1, 1]. The function should return the updated player position. The maze boundaries and obstacles are represented by '#' and the player's position is represented by 'P'. The function should not allow the player to move through walls or outside the maze boundaries.
"""

def move_player(maze, direction, player_position=[1, 1]):
    """
    Move the player within a given maze, considering the maze boundaries and obstacles.

    Args:
    maze (list): A 2D grid representing the maze.
    direction (str): The direction of movement (up, down, left, or right).
    player_position (list): The initial player position (default is [1, 1]).

    Returns:
    list: The updated player position.
    """

    new_position = player_position.copy()
    if direction == "up":
        new_position[0] -= 1
    elif direction == "down":
        new_position[0] += 1
    elif direction == "left":
        new_position[1] -= 1
    elif direction == "right":
        new_position[1] += 1

    # Check if the new position is within the maze boundaries and not a wall
    if (0 <= new_position[0] < len(maze) and 
        0 <= new_position[1] < len(maze[0]) and 
        maze[new_position[0]][new_position[1]] != '#'):
        player_position[0], player_position[1] = new_position[0], new_position[1]

    return player_position