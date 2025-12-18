"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods.
"""

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string