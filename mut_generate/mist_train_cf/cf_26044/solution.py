"""
QUESTION:
Remove duplicate characters from a given string and return the result as a string.

Given a string, write a function `remove_duplicate_chars` to remove duplicate characters from the string. The order of characters in the result should be the same as in the original string, and the function should not use any built-in string or set data structures to check for duplicate characters.
"""

def remove_duplicate_chars(s):
    char_set = [False] * 256
    result = ""

    for char in s:
        if not char_set[ord(char)]:
            char_set[ord(char)] = True
            result += char

    return result