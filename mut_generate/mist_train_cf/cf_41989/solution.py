"""
QUESTION:
Write a function `simulate_game(player_moves, obstacles, goal_position)` that simulates a simple game where a player moves left or right on a one-dimensional game board with positions represented by integers. The function takes in three parameters: a list of strings `player_moves` representing the player's movements, a set of integers `obstacles` representing the positions of obstacles, and an integer `goal_position` representing the position of the goal. The player starts at position 0 and valid movements move the player by one unit in the specified direction. The function should return "Player wins" if the player reaches the goal without colliding with obstacles, "Player loses" if the player collides with an obstacle, and "Player quits" if the player's movements lead to an invalid game state, such as moving beyond the game boundaries.
"""

from typing import List, Set

def entance(player_moves: List[str], obstacles: Set[int], goal_position: int) -> str:
    player_position = 0

    for move in player_moves:
        if move == "left":
            player_position -= 1
            if player_position < 0:
                return "Player quits"
        elif move == "right":
            player_position += 1
            if player_position in obstacles:
                return "Player loses"
            elif player_position == goal_position:
                return "Player wins"

    return "Player quits"