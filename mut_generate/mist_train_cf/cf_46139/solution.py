"""
QUESTION:
Create a function `character_count` that takes a string as input and returns a dictionary with unique characters as keys and their frequency in the string as values.
"""

def character_count(string):
    # Using a dictionary to store the character frequency
    char_count = {}

    # Going through each character in the string
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count