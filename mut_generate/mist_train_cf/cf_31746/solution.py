"""
QUESTION:
Implement a function called `reverse_string` that takes a string `input_string` as input and returns the reversed version of the string without using any built-in string reversal functions or slicing operations. The function should utilize a loop and basic string manipulation operations to achieve the result.
"""

def reverse_string(input_string):
    reversed_str = ''
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str