"""
QUESTION:
Create a function `replace_char` that takes in three parameters: a string, a character to be replaced, and a replacement character. The function should replace all instances of the specified character in the string while preserving the original capitalization and handling multilingual characters and emojis. The function should be case sensitive.
"""

def replace_char(string, char, replacement_char):
    new_string = ""
    for i in string:
        # check if character in string matches the character to replace
        if i == char:
            new_string += replacement_char
        else:
            new_string += i
    return new_string