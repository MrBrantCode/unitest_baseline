"""
QUESTION:
Create a function named `get_character_at_index` that takes a string and a non-negative integer index as input, and returns the character at the specified index in the string. The function should return an error message if the index is out of range. The input string can contain alphanumeric characters and special symbols.
"""

def get_character_at_index(string, index):
    if index < 0 or index >= len(string):
        return "Error: Index is out of range."
    return string[index]