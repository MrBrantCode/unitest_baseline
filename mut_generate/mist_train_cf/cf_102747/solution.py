"""
QUESTION:
Write a function `is_unique(string)` that determines if all characters in the input string are unique. The function should return `True` if all characters are unique and `False` otherwise.
"""

def is_unique(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return False
        char_count[char] = 1
    return True