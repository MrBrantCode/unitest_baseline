"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string. The function must use recursion and cannot use any loops or built-in string reversal functions or libraries.
"""

def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])