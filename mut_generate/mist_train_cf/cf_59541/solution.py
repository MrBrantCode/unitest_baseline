"""
QUESTION:
Create a function named `authenticate_characters` that takes two parameters: a character set (string) and a predetermined extent (integer). The function should return a string indicating whether the character set is legitimate (its length matches the predetermined extent) or not legitimate (its length does not match the predetermined extent).
"""

def authenticate_characters(character_set, predetermined_extent):
    """
    Authenticate the legitimacy of a character set based on its length and a predetermined extent.

    Args:
        character_set (str): The character set to be authenticated.
        predetermined_extent (int): The expected length of the character set.

    Returns:
        str: A message indicating whether the character set is legitimate or not.
    """

    # Check if the length of the character set is equal to the predetermined extent
    if len(character_set) == predetermined_extent:
        return "The character set is legitimate."
    # Check if the length of the character set is less than or greater than the predetermined extent
    elif len(character_set) < predetermined_extent or len(character_set) > predetermined_extent:
        return "The character set is not legitimate due to incorrect length."
    else:
        return "An error occurred during the authentication process."