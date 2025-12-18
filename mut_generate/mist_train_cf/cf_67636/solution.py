"""
QUESTION:
Write a function `to_uppercase(string)` that takes a string as input and returns the string with all letters converted to uppercase, without using the built-in `upper()` method. The function should handle both English and non-English characters, including those from the Cyrillic and Greek alphabets, and should preserve punctuation marks and other non-letter characters.
"""

def to_uppercase(string):
    result = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        elif ord(char) >= 224 and ord(char) <= 255:
            result += chr(ord(char) - 32)
        elif ord(char) >= 1072 and ord(char) <= 1103:
            result += chr(ord(char) - 32)
        elif ord(char) >= 945 and ord(char) <= 969:
            result += chr(ord(char) - 32)
        else:
            result += char
    return result