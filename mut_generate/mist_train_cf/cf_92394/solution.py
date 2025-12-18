"""
QUESTION:
Create a function called `sort_string_descending` that takes one parameter, a string. The function should sort the characters in the string in alphabetical order, but in descending order (Z to A). The function should return the sorted string.
"""

def sort_string_descending(string):
    return ''.join(sorted(string, reverse=True))