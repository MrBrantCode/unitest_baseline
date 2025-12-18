"""
QUESTION:
Write a function named `replace_x_with_y` that replaces all occurrences of 'x' with 'y' in a given string without using any built-in string manipulation functions or regular expressions. The function must achieve this in a time complexity of O(n) and use only constant space. The input string can contain any characters, including spaces and punctuation.
"""

def replace_x_with_y(s):
    new_str = ""
    for char in s:
        if char == 'x':
            new_str += 'y'
        else:
            new_str += char
    return new_str