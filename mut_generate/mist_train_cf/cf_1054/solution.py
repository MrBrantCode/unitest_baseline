"""
QUESTION:
Implement a function named `to_uppercase` that takes a string as input and returns the string in uppercase without using any built-in string methods or functions that directly manipulate strings. The function should handle all types of characters, including alphabets, numbers, and special characters, and should work efficiently for strings of any length. The implementation must be recursive and should not use any pre-defined lists or dictionaries, external libraries, or modules, and should minimize the use of unnecessary variables.
"""

def to_uppercase(string):
    if len(string) == 0:
        return ""
    else:
        char = string[0]
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        return char + to_uppercase(string[1:])