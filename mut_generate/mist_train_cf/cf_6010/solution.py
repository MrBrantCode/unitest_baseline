"""
QUESTION:
Create a function `replace_zeros` that takes a list `input_list` as input and replaces all occurrences of 0 with 1. The function should handle nested lists and preserve their original structure, only using recursion to iterate through the list and make replacements, without utilizing any additional data structures or built-in Python functions.
"""

def replace_zeros(input_list):
    if isinstance(input_list, list):
        for i in range(len(input_list)):
            if isinstance(input_list[i], list):
                input_list[i] = replace_zeros(input_list[i])
            elif input_list[i] == 0:
                input_list[i] = 1
    elif input_list == 0:
        input_list = 1
    return input_list