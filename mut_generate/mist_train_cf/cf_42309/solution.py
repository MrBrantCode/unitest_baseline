"""
QUESTION:
Implement a function `remove_all` that takes a string `s` and a character `c` as parameters, and returns the string `s` with all occurrences of `c` removed. The function should not use any built-in string manipulation functions.
"""

def remove_all(s, c):
    result = ''
    for char in s:
        if char != c:
            result += char
    return result