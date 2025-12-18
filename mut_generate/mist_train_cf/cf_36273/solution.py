"""
QUESTION:
Implement the `adventure_game` function, which takes a string as player's input and returns the outcome of their choices in a text-based adventure game. The game starts at a fork in a forest where the player can choose to go "left" or "right". If the player goes left, they encounter a river and can choose to "swim" across or find a "bridge". If the player goes right, they encounter a cave and can choose to "enter" the cave or "continue" along the path. The function should return a string describing the outcome based on the player's choices. The function should handle the inputs "left", "right", "swim", "bridge", "enter", and "continue".
"""

def adventure_game(player_input: str) -> str:
    if player_input == "left":
        return "You chose to go left. You encounter a river. Do you want to swim across or find a bridge?"
    elif player_input == "right":
        return "You chose to go right. You encounter a cave. Do you want to enter the cave or continue along the path?"
    elif player_input == "swim":
        return "You chose to swim across the river. You made it to the other side and found a treasure!"
    elif player_input == "bridge":
        return "You chose to find a bridge. You safely cross the river and find a map leading to a hidden treasure!"
    elif player_input == "enter":
        return "You chose to enter the cave. Inside, you find a wild animal and narrowly escape!"
    elif player_input == "continue":
        return "You chose to continue along the path. You get lost in the forest and find your way back after a long journey."
    else:
        return "Invalid input. Please choose a valid option."