"""
QUESTION:
Write a recursive function named `reverse_string` that takes a string `input_str` as input and returns the reversed string without using any built-in function or additional temporary variable except for recursion variables.
"""

def reverse_string(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return reverse_string(input_str[1:]) + input_str[0]