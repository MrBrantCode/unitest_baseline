"""
QUESTION:
Create a function called `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or slicing.
"""

def entrance(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string