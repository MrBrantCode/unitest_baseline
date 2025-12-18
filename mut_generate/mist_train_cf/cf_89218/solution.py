"""
QUESTION:
Write a function called `replace_zeros` that takes a list `input_list` as input and returns the modified list with all 0s replaced with 1s, including nested lists. The function should use recursion and not use any additional data structures or built-in Python functions. It should handle integers and nested lists only, without modifying other numbers.
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