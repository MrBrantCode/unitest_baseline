"""
QUESTION:
Create a function `remove_duplicates` that takes a list of strings as input, removes duplicates while maintaining the original order of appearance, and returns the list of unique strings without using any built-in Python functions or libraries for handling duplicates.
"""

def remove_duplicates(strings):
    non_duplicates = {}
    for string in strings:
        if string not in non_duplicates:
            non_duplicates[string] = None
    return list(non_duplicates.keys())