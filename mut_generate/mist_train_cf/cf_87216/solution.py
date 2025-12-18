"""
QUESTION:
Write a function `convert_string_to_list` that takes a string as input and returns a list of characters. The function should remove any non-alphabetic characters except for spaces and collapse multiple consecutive spaces into a single space. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

import string

def convert_string_to_list(string_input):
    characters = []
    for char in string_input:
        if char.isalpha() or char.isspace():
            if char in string.punctuation:
                continue
            characters.append(char)

    processed_string = ''.join(characters)
    processed_string = ' '.join(processed_string.split())

    characters = list(processed_string)

    return characters