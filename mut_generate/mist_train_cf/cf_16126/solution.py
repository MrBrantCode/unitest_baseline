"""
QUESTION:
Write a function called `reverse_string` that takes a string of lowercase English letters as input and returns the reversed string without using the built-in `reverse()` method or any other string manipulation methods.
"""

def reverse_string(s):
    reversed_string = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string