"""
QUESTION:
Create a function called `remove_character` that takes two parameters: a string and a character. The function should remove all occurrences of the given character from the string, treating uppercase and lowercase characters as the same.
"""

def remove_character(string, character):
    modified_string = ""
    character = character.lower()

    for char in string:
        char = char.lower()
        if char != character:
            modified_string += char

    return modified_string