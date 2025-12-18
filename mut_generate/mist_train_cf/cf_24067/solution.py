"""
QUESTION:
Create a function `reverse` that takes a string as input and returns the reversed string. The function should not use any built-in string reversal methods.
"""

def reverse(s):
    str = "" 
    for i in s: 
        str = i + str 
    return str