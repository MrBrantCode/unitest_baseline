"""
QUESTION:
Write a Python function named `replace_with_next_consecutive_char` that takes a string as input, replaces each alphabetic character with the next consecutive character in the alphabet (wrapping around from 'z' to 'a' and from 'Z' to 'A' if necessary), and ignores non-alphabetic characters. The function should handle both uppercase and lowercase letters separately.
"""

def replace_with_next_consecutive_char(string):
    result = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    result += 'a'
                else:
                    result += chr(ord(char) + 1)
            elif char.isupper():
                if char == 'Z':
                    result += 'A'
                else:
                    result += chr(ord(char) + 1)
        else:
            result += char
    return result