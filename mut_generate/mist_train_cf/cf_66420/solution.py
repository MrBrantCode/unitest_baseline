"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions or methods.
"""

def reverse_string(s):
    reversed_s = ''
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s