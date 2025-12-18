"""
QUESTION:
Create a function `replace_characters(s)` that takes a string `s` as input. The function should replace each alphabetic character in the string with the next character in alphabetic order, wrapping around from 'z' to 'a' and 'Z' to 'A', while ignoring any special characters or digits. The function should return a string of the same length as the input string.
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