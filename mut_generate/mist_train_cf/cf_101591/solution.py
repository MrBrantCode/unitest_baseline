"""
QUESTION:
Write a function `check_characters` that checks whether a given set of characters contains 'A' and any duplicate characters. The function should return a boolean value indicating the presence of 'A' and duplicates. The input character set is guaranteed to be a string of alphabets without any whitespace or special characters. The function should not connect to any database or output the results in a specific format.
"""

def check_characters(character_set):
    """
    Checks whether a given set of characters contains 'A' and any duplicate characters.

    Args:
        character_set (str): A string of alphabets without any whitespace or special characters.

    Returns:
        bool: A boolean value indicating the presence of 'A' and duplicates.
    """
    has_a = 'A' in character_set
    has_duplicates = len(set(character_set)) != len(character_set)
    return has_a and has_duplicates