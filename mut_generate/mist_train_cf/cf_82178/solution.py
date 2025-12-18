"""
QUESTION:
Write a function `modify_string(s)` that takes a string `s` as input and attempts to modify its first character. The function should capture and return any exception raised due to the immutability of strings in Python.
"""

def modify_string(s):
    try:
        s[0] = 'T'
    except TypeError as e:
        return 'Exception encountered:', str(e)