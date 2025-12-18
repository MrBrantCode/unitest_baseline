"""
QUESTION:
Create a function named `replace_characters` that takes a string `s` as input. Replace each alphabetic character in the string with the next character in alphabetic order, wrapping around from 'z' to 'a' and 'Z' to 'A', while ignoring any non-alphabetic characters. The output string should have the same length as the input string.
"""

def replace_characters(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                if char == 'z':
                    result += 'a'
                else:
                    result += chr(ord(char) + 1)
            else:
                if char == 'Z':
                    result += 'A'
                else:
                    result += chr(ord(char) + 1)
        else:
            result += char
    return result