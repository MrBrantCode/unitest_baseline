"""
QUESTION:
Implement a recursive function named `to_uppercase` that takes a string as input and returns the string in uppercase without using any built-in string methods, external libraries, pre-defined lists or dictionaries. The function should handle all types of characters, including alphabets, numbers, and special characters, and work efficiently for strings of any length. The function should minimize the use of unnecessary variables and optimize for performance.
"""

def to_uppercase(string):
    if len(string) == 0:
        return ""
    else:
        char = string[0]
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        return char + to_uppercase(string[1:])