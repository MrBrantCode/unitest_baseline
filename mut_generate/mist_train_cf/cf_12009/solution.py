"""
QUESTION:
Write a function `count_characters(string)` that takes a string as input and returns a dictionary containing the count of all characters (excluding whitespace) in a case-insensitive manner.
"""

def count_characters(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char.isspace():
            continue
        char_count[char] = char_count.get(char, 0) + 1
    return char_count