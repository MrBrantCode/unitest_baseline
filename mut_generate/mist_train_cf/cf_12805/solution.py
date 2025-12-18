"""
QUESTION:
Create a function `count_unique_characters` that takes a string as input and returns the number of unique characters in the string, excluding those that are surrounded by quotation marks. The function should consider a pair of quotation marks as the boundary and ignore any characters between them. The input string can contain any ASCII characters and can have multiple pairs of quotation marks.
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