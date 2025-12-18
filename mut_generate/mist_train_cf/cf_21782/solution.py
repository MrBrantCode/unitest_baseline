"""
QUESTION:
Create a function called `find_last_occurrence` that takes two parameters: `string` and `character`. The function should return the index of the last occurrence of `character` in `string` without using built-in string manipulation methods or functions. If `character` is not found in `string`, return -1. The solution should have a time complexity of O(n), where n is the length of the string.
"""

def find_last_occurrence(string, character):
    last_index = -1
    for i in range(len(string)):
        if string[i] == character:
            last_index = i
    return last_index