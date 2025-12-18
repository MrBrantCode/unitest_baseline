"""
QUESTION:
Write a function `replace_A_with_Z` that takes a string as an argument and returns a new string where all instances of 'A' are replaced with 'Z' without using any built-in string replacement functions.
"""

def replace_A_with_Z(s):
    new_string = ''
    for char in s:
        if char == 'A':
           new_string += 'Z'
        else:
           new_string += char
    return new_string