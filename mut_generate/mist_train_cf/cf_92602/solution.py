"""
QUESTION:
Create a function called `remove_whitespace_and_duplicates` that takes a string as input. This function should remove all whitespace from the string and eliminate any duplicate characters, preserving the original order of characters. The function should not use any built-in string or list methods for removing duplicates or whitespace, except for the `list` function to convert the string to a list of characters and the `join` function to convert the list back to a string.
"""

def remove_whitespace_and_duplicates(string):
    chars = list(string)
    unique_chars = []
    
    for char in chars:
        if char != ' ' and char not in unique_chars:
            unique_chars.append(char)
    
    return ''.join(unique_chars)