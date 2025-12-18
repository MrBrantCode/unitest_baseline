"""
QUESTION:
Write a function named `reverse_string` that takes an input string and returns the string in reversed order without using any pre-existing methods or looping constructs. The function should be able to handle strings of any length, including empty strings.
"""

def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]