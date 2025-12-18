"""
QUESTION:
Create a function `is_character_in_string` that takes two parameters: `string` and `character`. Without using built-in string methods, implement a way to determine if the `character` is present in the `string`. The function should return `True` if the `character` is found and `False` otherwise.
"""

def is_character_in_string(string, character):
    for char in string:
        if char == character:
            return True
    return False