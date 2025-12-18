"""
QUESTION:
Create a function named `string_to_list` that takes a string as input and returns a list of characters from the string, excluding any whitespace characters. Do not use built-in string or list methods to achieve the result.
"""

def string_to_list(string):
    char_list = []
    for char in string:
        if char != ' ':
            char_list.append(char)
    return char_list