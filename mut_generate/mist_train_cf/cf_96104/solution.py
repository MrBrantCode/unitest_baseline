"""
QUESTION:
Write a function `reverse_string(input_string)` that takes a string as input and returns a single string composed of all the characters of the given string, one after the other, in reverse order, without using any built-in string reversal functions or methods.
"""

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string