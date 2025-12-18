"""
QUESTION:
Create a function called `remove_string` that takes two parameters: `remove` (the string to be removed) and `string` (the original string). The function should return the modified string with all occurrences of `remove` removed from `string`.
"""

def remove_string(remove, string):
    return string.replace(remove, "")