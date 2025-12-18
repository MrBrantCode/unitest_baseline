"""
QUESTION:
Write a recursive function named `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]