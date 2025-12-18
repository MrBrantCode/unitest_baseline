"""
QUESTION:
Write a function `find_character` that takes in a string and a lowercase alphabet character. The string has a maximum length of 1000 characters and does not contain leading or trailing whitespace. Return the index of the first occurrence of the character in the string. If the character is not found, return -1. Do not use built-in string or array methods such as `indexOf`, `find`, or `includes`. Implement your own logic to search for the character in the string.
"""

def find_character(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
    return -1