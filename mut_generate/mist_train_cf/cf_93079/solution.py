"""
QUESTION:
Create a function called `reverse_string` that takes a string `s` as input, where `s` has at most 1000 lowercase letters, and returns a new string with the same characters but in reverse order, without using any built-in reverse functions or methods.
"""

def entrance(s):
    reversed_str = ''
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str