"""
QUESTION:
Write a function `replace_next_char` that takes a string as input and returns a new string where each alphabetic character is replaced by the next character in alphabetical order. The function should preserve the case of the original characters, leaving non-alphabetic characters unchanged.
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
                result += next_char if char.islower() else next_char.upper()
        else:
            result += char
    return result