"""
QUESTION:
Write a function called `convert_to_uppercase` that takes a string `s` as input, converts all lowercase letters to uppercase using the ASCII table, and returns the modified string. The function should handle both lowercase and uppercase letters, and any non-alphabetic characters should remain unchanged.
"""

def convert_to_uppercase(s):
    result = ""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result