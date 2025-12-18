"""
QUESTION:
Write a function named `reverse_string` that takes an input string and returns the reversed string. The function should be case sensitive and handle special characters and whitespaces efficiently without using any built-in string reversal functions or methods.
"""

def reverse_string(s):
    reverse = ''
    for character in s:
        reverse = character + reverse
    return reverse