"""
QUESTION:
Write a function `reverse_string` that takes an input string and returns the string in reverse order without using any built-in string reversal functions or operators.
"""

def reverse_string(input_str):
    reversed_str = ''
    for c in input_str:
        reversed_str = c + reversed_str
    return reversed_str