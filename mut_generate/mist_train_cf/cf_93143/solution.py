"""
QUESTION:
Write a function named `reverse_string` that takes a string `input_string` as input, reverses it without using any built-in string reversal functions or methods, and returns the reversed string. The input string can contain any printable ASCII characters.
"""

def reverse_string(input_string):
    reversed_string = ""

    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]

    return reversed_string