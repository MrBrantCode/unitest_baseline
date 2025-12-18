"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string. The function should not use any pre-defined functions (excluding list manipulation and string joining, which are inherent features in Python) or extra variables.
"""

def entrance(input_str):
    input_str = list(input_str)
    length = len(input_str)
    for i in range(length//2):
        input_str[i], input_str[length-i-1] = input_str[length-i-1], input_str[i]
    return ''.join(input_str)