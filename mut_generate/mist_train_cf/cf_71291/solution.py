"""
QUESTION:
Implement the function `remove_characters(name, characters)` that takes two parameters: a string `name` and a list of characters `characters`. The function should return a new string where all occurrences of characters in the `characters` list have been removed from the `name` string. The function should be efficient enough to handle large input strings.
"""

def remove_characters(name, characters):
    for character in characters:
        name = name.replace(character, '')
    return name