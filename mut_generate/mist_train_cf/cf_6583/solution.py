"""
QUESTION:
Write a function `remove_characters(name, characters)` that removes all occurrences of the characters in `characters` from the `name` string. The function should return the modified `name` string.

The input `name` string consists of alphanumeric characters (a-z, A-Z, 0-9) and spaces. The input `characters` list consists of alphanumeric characters (a-z, A-Z, 0-9). The length of `name` is at most 10^5 characters and the length of `characters` is at most 10^3. The function should have a time complexity of O(n), where n is the length of the `name` string.
"""

def remove_characters(name, characters):
    new_name = ""
    for c in name:
        if c not in characters:
            new_name += c
    return new_name