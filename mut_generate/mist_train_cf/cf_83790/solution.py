"""
QUESTION:
Create a function `unique_char_index(s)` that finds the index of the first non-repeating character in a given string `s`. If all characters in the string are repeating or the string is empty, the function should return -1. The function should support strings containing special characters and Unicode characters.
"""

def unique_char_index(s):
    character_map = {}
    for i, char in enumerate(s):
        if char in character_map:
            character_map[char].append(i)
        else:
            character_map[char] = [i]
    for char in s:
        if len(character_map[char]) == 1:
            return character_map[char][0]
    return -1