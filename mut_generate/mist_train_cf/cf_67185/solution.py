"""
QUESTION:
Write a function called `is_char_at_position` that takes a string of mixed letters and numbers, a specific character, and a 1-indexed position number as input. The function should return a boolean value indicating whether the specific character appears at the specified position in the string.
"""

def is_char_at_position(string, char, num):
    return string[num-1] == char