"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string without using any built-in string reversal functions. The function should be able to handle special characters and white spaces. Note that the input string can be modified but the function should not use any existing string reversal methods. The function should return a new string with the characters in reverse order.
"""

def reverse_string(s):
    rev_str = ""
    for i in s:
        rev_str = i + rev_str
    return rev_str