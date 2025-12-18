"""
QUESTION:
Implement a function `reverse(s)` that takes a string `s` as input and returns the reversed string. The function should only accept a string as input and return a string as output, without using any built-in string reversal functions or methods.
"""

def reverse(s):
    rev = ""
 
    i = len(s)
    while i > 0:
        rev += s[ i - 1 ]
        i = i - 1
 
    return rev