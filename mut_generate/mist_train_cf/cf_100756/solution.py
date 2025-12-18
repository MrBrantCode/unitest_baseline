"""
QUESTION:
Create a function called `reverse_string` that takes a string argument and returns the reversed string using recursion. The function should be able to handle strings of any length.
"""

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]