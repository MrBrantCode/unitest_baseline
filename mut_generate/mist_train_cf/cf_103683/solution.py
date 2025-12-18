"""
QUESTION:
Create a `Player` class with a private `name` attribute of type string and two public methods: `setName(name: str)` and `getName()`. The `setName` method should set the `name` attribute to the provided string if it meets the following conditions: the string length is between 3 and 20 characters (inclusive), and the string contains only alphabetic characters. The `getName` method should return the value of the `name` attribute.
"""

def set_name(player_name: str) -> str or None:
    """
    Sets the player's name if the provided string meets the conditions.
    
    Args:
        player_name (str): The name to be set.
    
    Returns:
        str: The set name if conditions are met, otherwise None.
    """
    if 3 <= len(player_name) <= 20 and player_name.isalpha():
        return player_name
    else:
        return None