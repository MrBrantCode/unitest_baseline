"""
QUESTION:
Write a function named "reverse_string" that takes a string as input and returns the string with its characters in reverse order. You are not allowed to use any built-in string manipulation functions or methods, and the solution must achieve a time complexity of O(n).
"""

def reverse_string(s):
    return ''.join([char for char in s[::-1]])