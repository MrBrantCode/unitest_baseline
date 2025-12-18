"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns its reverse. The function should not use any built-in string manipulation functions or methods.
"""

def reverse_string(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str