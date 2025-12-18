"""
QUESTION:
Create a function `remove_adjacent_duplicates` that takes a string as input and returns a modified string where all duplicate characters that are adjacent to each other are removed.
"""

def remove_adjacent_duplicates(s):
    result = ""
    prev_char = None
    for char in s:
        if char != prev_char:
            result += char
        prev_char = char
    return result