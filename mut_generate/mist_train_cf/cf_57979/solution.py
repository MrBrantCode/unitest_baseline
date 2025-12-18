"""
QUESTION:
Create a function called `replace_digits_with_asterisks` that takes a string as input and returns a new string where all digit characters are replaced with asterisk symbols.
"""

def replace_digits_with_asterisks(input_string):
    result = ""
    for char in input_string:
        if char.isdigit():
            result += "*"
        else:
            result += char
    return result