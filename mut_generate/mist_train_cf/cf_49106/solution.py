"""
QUESTION:
Create a function named `reverse_string` that takes a sequence of characters as input and returns the reversed sequence without using built-in reverse functions or methods.
"""

def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]