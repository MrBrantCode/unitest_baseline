"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the string with its characters in reverse order, without using any built-in string reversal functions or methods in Python. The function should work for any given string.
"""

def reverse_string(input_string):
    reversed_str = ''
    index = len(input_string)

    while index:  
        index -= 1  
        reversed_str += input_string[index]  

    return reversed_str