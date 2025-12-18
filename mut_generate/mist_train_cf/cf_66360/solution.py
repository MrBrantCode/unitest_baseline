"""
QUESTION:
Write a function called `reverse_string` that takes a string `input_string` as input and returns the string with its characters reversed. Do not use any built-in string reversal functions.
"""

def reverse_string(input_string):
    reversed_string = ''
    for i in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string