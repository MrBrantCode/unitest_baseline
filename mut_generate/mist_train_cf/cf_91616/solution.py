"""
QUESTION:
Create a function named `reverse_string` that takes a string as input and returns the reversed string. The function should not use any built-in string manipulation functions or libraries.
"""

def reverse_string(s):
    reversed_s = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s