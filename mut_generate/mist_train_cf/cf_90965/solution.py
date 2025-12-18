"""
QUESTION:
Write a function called `reverse_string` that takes a string `input_str` as input and returns the reversed string without using any built-in string reversal functions or methods.
"""

def reverse_string(input_str):
    reversed_str = ""
    for i in range(len(input_str)-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str