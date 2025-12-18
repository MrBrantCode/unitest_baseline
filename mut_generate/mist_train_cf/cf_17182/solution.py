"""
QUESTION:
Create a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or methods and without using any loops.
"""

def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]