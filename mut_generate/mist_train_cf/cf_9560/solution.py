"""
QUESTION:
Write a function `delete_character` that takes a string and a character as input and returns the string with all occurrences of the given character removed, ignoring the case of the characters in the string. The function should handle cases where the given character appears multiple times in the string.
"""

def delete_character(string, character):
    # Convert the character to lowercase to ignore case
    character = character.lower()
    
    # Remove all occurrences of the character from the string
    new_string = string.lower().replace(character, "")
    
    return new_string