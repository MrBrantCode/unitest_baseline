"""
QUESTION:
Write a function named `shift_string` that takes a string `s` as input, shifts each alphabetic character to the next sequential character in the alphabet (wrapping around from 'z' or 'Z' to 'a' or 'A'), and leaves non-alphabetic characters unchanged.
"""

def shift_string(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.lower() == 'z':
                result += 'a' if char.islower() else 'A'
            else:
                result += chr(ord(char) + 1)
        else:
            result += char
    return result