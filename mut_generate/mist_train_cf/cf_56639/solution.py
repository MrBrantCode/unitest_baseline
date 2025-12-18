"""
QUESTION:
Create a function named `reverse_string` that takes a single parameter `input_str`. The function should return the reversed version of `input_str` if it's a string; otherwise, return an error message.
"""

def reverse_string(input_str):
    if isinstance(input_str, str):  # check if input is a string
        return input_str[::-1]  # the [::-1] slice reverses a string in Python
    else:
        return "The provided input is not a string."