"""
QUESTION:
Write a recursive function called `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string manipulation functions or data structures. The function should use recursion to reverse the string, with a base case for when the length of the string is 0.
"""

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]