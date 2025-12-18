"""
QUESTION:
Create a function `first_non_repeating_character` that takes a string as input and returns the first non-repeating character in the string, considering the comparison case-insensitive. The function should return None if no non-repeating character is found.
"""

def first_non_repeating_character(s):
    s = s.lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None