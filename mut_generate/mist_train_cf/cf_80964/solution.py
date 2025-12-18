"""
QUESTION:
Write a function `increment_string(s)` that increments each character in a given string `s` by one. If the character is a letter, it should wrap around to the beginning of the alphabet if necessary (i.e., 'z' becomes 'a' and 'Z' becomes 'A'). Non-alphabetic characters should remain unchanged.
"""

def increment_string(s):
    result = ""
    for char in s:
        if char.isupper():
            result += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        else:
            result += char
    return result