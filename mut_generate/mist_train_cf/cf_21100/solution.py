"""
QUESTION:
Implement a function named `replace_characters(input_str)` that takes a string of alphabetic characters (both uppercase and lowercase) as input and returns a string where each character is replaced by the next character in alphabetic order, wrapping around from 'z' to 'a' and 'Z' to 'A'. The input string can be empty and the output string should have the same length as the input string.
"""

def replace_characters(input_str):
    result = ""
    for c in input_str:
        if c.isupper():
            next_char = chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            next_char = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        result += next_char
    return result