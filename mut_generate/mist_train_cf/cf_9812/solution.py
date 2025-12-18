"""
QUESTION:
Implement a function `replace_x_with_y` that takes a string `sentence` as input and returns the string with all occurrences of 'x' replaced with 'y'. The function must not use any built-in string manipulation functions or regular expressions.
"""

def replace_x_with_y(sentence):
    result = ""
    for char in sentence:
        if char == 'x':
            result += 'y'
        else:
            result += char
    return result