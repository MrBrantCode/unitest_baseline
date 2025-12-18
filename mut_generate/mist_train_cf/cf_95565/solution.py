"""
QUESTION:
Write a function named `reverse_string` that takes a string `input_string` as input and returns a new string that is the reverse of the `input_string`. The function should not use any built-in functions or methods that directly reverse a string.
"""

def entance(input_string):
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    return reversed_string