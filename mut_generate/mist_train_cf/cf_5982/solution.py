"""
QUESTION:
Create a function called `remove_whitespace_duplicates` that takes a string as input and returns the string after removing all whitespace characters, duplicates, and punctuation marks. The order of the remaining characters should be preserved.
"""

import string

def remove_whitespace_duplicates(input_string):
    unique_characters = []
    characters_list = list(input_string)
    
    for character in characters_list:
        if character.isspace():
            continue
        if character in string.punctuation:
            continue
        if character not in unique_characters:
            unique_characters.append(character)
    
    result_string = ''.join(unique_characters)
    return result_string