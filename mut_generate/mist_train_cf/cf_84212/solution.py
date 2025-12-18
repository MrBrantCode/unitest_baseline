"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input and returns a new string where all duplicate characters are removed, preserving the order of the first occurrence of each character. The function should not use any built-in data structures other than strings.
"""

def remove_duplicates(s):
    result = ''
    for char in s:
        if char not in result:
            result += char
    return result