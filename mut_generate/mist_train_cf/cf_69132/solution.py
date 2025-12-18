"""
QUESTION:
Create a function `rep_string` that takes a string `s` and a non-negative integer `n` as arguments. The function should return the string `s` repeated `n` times without using Python's built-in repeat operator (`*`) or a loop, instead utilizing recursion. Ensure proper handling of edge cases, such as an empty string input or a zero number input.
"""

def rep_string(s, n):
    if n == 0: 
        return ""
    elif n == 1: 
        return s
    else: 
        return s + rep_string(s, n-1)