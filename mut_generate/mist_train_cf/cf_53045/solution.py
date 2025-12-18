"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string using a loop structure.
"""

def entance(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s