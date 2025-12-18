"""
QUESTION:
Write a function named `convert_to_uppercase` that takes a string `s` as input and returns the string converted to uppercase. The function should use only basic string manipulation operations, have a time complexity of O(n) where n is the length of the string, and not use any built-in string manipulation functions or regular expressions. The input string may contain punctuation marks, special characters, and spaces.
"""

def convert_to_uppercase(s):
    result = ''
    for c in s:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result