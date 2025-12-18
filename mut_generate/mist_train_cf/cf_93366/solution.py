"""
QUESTION:
Write a function `is_character_in_string` that determines if a particular character is included in a given string without using built-in string manipulation or character checking methods. The function should take two parameters: `string` (the string to search within) and `character` (the character to search for). Return `True` if the character is found in the string, and `False` otherwise.
"""

def is_character_in_string(string, character):
    for char in string:
        if char == character:
            return True
    return False