"""
QUESTION:
Given a string of up to 1000 characters with no leading or trailing whitespace and a lowercase alphabet character, write a function `find_first_index(string, character)` that returns the first index at which the character appears in the string. If the character is not found, return -1.
"""

def find_first_index(string, character):
    for i in range(len(string)):
        if string[i] == character:
            return i
    return -1  # return -1 if the character is not found