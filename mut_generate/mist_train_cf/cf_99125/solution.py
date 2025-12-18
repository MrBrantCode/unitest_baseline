"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the reversed string without using any loops, built-in string reversal functions, or libraries. The function should use recursion to reverse the string.
"""

def entance(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + entance(string[:-1])