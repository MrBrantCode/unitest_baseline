"""
QUESTION:
Write a function `replace_x_with_y` that takes a string `sentence` as input and returns a new string where all occurrences of 'x' are replaced with 'y'. Do not use any built-in string manipulation functions or regular expressions. Implement your own algorithm to achieve the desired result.
"""

def replace_x_with_y(sentence):
    result = ""
    for char in sentence:
        if char == 'x':
            result += 'y'
        else:
            result += char
    return result