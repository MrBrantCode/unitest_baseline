"""
QUESTION:
Write a function `remove_character(string, index)` that takes a nonempty string and an integer index as input, removes the character at the specified index from the string, and returns a tuple containing the modified string and the total number of characters removed. If the given index is out of range, the function should return the original string and 0 as the total number of characters removed.
"""

def remove_character(string, index):
    removed_chars = 0
    if index < 0 or index >= len(string):
        return string, removed_chars
    else:
        modified_string = string[:index] + string[index + 1:]
        removed_chars = 1
        return modified_string, removed_chars