"""
QUESTION:
Write a function called `reverse_string` that takes a string of lowercase letters as input and returns the same set of characters in reverse order without using any built-in reverse functions or methods, or any functions/methods that directly manipulate strings. The input string will contain at least one character and at most 1000 characters.
"""

def reverse_string(input_str):
    reversed_str = ''
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str