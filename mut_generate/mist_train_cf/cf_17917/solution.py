"""
QUESTION:
Remove duplicated characters from a given string and return the output in ascending order based on ASCII values of the characters. The function should be named `remove_duplicates` and take one string argument.
"""

def remove_duplicates(string):
    unique_chars = list(set(string))
    unique_chars.sort()
    return ''.join(unique_chars)