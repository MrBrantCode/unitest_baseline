"""
QUESTION:
Create a function `replace_characters(input_str)` that takes a string of alphabetic characters as input, replaces each character with the next character in alphabetic order (wrapping around from 'z' to 'a' and 'Z' to 'A'), and returns the resulting string. The input string can be empty and may contain both uppercase and lowercase letters. The output string should have the same length as the input string.
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