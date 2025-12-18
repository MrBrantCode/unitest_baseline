"""
QUESTION:
Create a function that simulates weight resistance when a player attempts to lift an object beyond their capacity. The function should take two parameters: `player_strength` and `object_weight`, where `player_strength` represents the player's maximum lifting capacity and `object_weight` represents the weight of the object being lifted. The function should return a boolean value indicating whether the object is too heavy for the player to lift.
"""

def is_too_heavy(player_strength, object_weight):
    """
    Returns True if the object is too heavy for the player to lift, False otherwise.

    Parameters:
    player_strength (int): The player's maximum lifting capacity.
    object_weight (int): The weight of the object being lifted.

    Returns:
    bool: Whether the object is too heavy for the player to lift.
    """
    return player_strength < object_weight