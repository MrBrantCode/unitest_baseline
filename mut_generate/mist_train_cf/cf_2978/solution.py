"""
QUESTION:
Write a function named `string_length` that takes a string as input and returns the length of the string without using any built-in length functions, methods, loops, or recursion.
"""

def string_length(s):
    return sum(1 for _ in map(ord, s))