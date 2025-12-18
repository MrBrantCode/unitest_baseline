"""
QUESTION:
Write a function `string_length` that calculates the length of a given string without using built-in string length functions, methods, loops, or recursion.
"""

def string_length(s):
    return sum(1 for _ in map(ord, s))