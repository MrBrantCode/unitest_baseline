"""
QUESTION:
Implement a function `convert_to_uppercase(s)` that takes a string `s` as input and returns its uppercase equivalent. The function should only use basic string manipulation operations, and should not use built-in string manipulation functions or regular expressions. The time complexity of the function should be O(n), where n is the length of the string.
"""

def convert_to_uppercase(s):
    result = ''
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result