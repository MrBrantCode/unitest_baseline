"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input and returns a new string with all duplicate characters removed. The function should preserve the original order of characters.
"""

def remove_duplicates(string):
    new_string = ""
    for char in string:
        if char not in new_string:
            new_string += char
    return new_string