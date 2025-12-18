"""
QUESTION:
Create a function `count_unique_characters(input_string)` that takes a string as input and returns the number of unique characters in the string, excluding any characters that are surrounded by double quotation marks (`"`) in the input string. The function should ignore the quotation marks themselves and only consider the characters outside the quoted sections.
"""

def count_unique_characters(input_string):
    unique_chars = set()
    is_quoted = False
    
    for char in input_string:
        if char == '"':
            is_quoted = not is_quoted
        elif not is_quoted:
            unique_chars.add(char)
    
    return len(unique_chars)