"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns its reverse. Do not use any built-in string manipulation functions or methods.
"""

def entrance(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str