"""
QUESTION:
Write a function named `custom_reverse_string` that takes a string `s` as input and returns the reverse of the string without using any built-in Python functions for reversing. The function should handle Unicode characters correctly.
"""

def custom_reverse_string(s):
    reversed_string = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string