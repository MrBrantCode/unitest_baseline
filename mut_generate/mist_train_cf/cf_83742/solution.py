"""
QUESTION:
Create a function `remove_duplicates(string)` that takes a string of alphabetic elements as input and returns a new string with all consecutive duplicate characters removed.
"""

def remove_duplicates(string):
    new_string = ''
    last_char = None
    for char in string:
        if char != last_char:
            new_string += char
            last_char = char
    return new_string