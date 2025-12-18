"""
QUESTION:
Implement a function `replace_next_char` that replaces each character in a given string with the next character in alphabetical order. The function should handle both uppercase and lowercase letters, wrapping around from 'z' to 'a' and 'Z' to 'A', and leave non-alphabetic characters unchanged.
"""

def replace_next_char(string):
    result = ""
    for char in string:
        if char.isalpha():
            if char == 'z':
                result += 'a' if char.islower() else 'A'
            elif char == 'Z':
                result += 'A' if char.isupper() else 'a'
            else:
                next_char = chr(ord(char) + 1)
                result += next_char if char.islower() else chr(ord(char) + 1)
        else:
            result += char
    return result