"""
QUESTION:
Write a function named `reverse_string` that takes a string as an argument and returns the reversed string. The function must not use loops or any built-in string reversal functions or libraries.
"""

def reverse_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string(string[:-1])