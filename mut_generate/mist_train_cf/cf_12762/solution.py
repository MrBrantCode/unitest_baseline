"""
QUESTION:
Write a function `remove_adjacent_duplicates` that takes a string as an argument, removes all duplicate characters that are adjacent to each other, and returns the modified string.
"""

def remove_adjacent_duplicates(s):
    result = ""
    prev_char = None
    for char in s:
        if char != prev_char:
            result += char
        prev_char = char
    return result