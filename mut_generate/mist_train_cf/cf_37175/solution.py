"""
QUESTION:
Implement the `make_filename` function, which takes a player's name as input and returns a string representing the filename in the format "playername.txt", where "playername" is the lowercase version of the player's name with spaces replaced by underscores.
"""

def make_filename(player_name):
    """
    Generates a filename for the player based on the given name.

    Args:
    player_name (str): The name of the player.

    Returns:
    str: The filename in the format "playername.txt".
    """
    return player_name.lower().replace(' ', '_') + '.txt'