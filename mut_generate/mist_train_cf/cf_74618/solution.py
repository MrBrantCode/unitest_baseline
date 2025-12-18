"""
QUESTION:
Create a function called `advanced_cryptography` that takes a string `s` and an integer `shift` as parameters. The function should shift each letter in the string by `3 * shift` positions down the alphabet, preserving the case of alphabets and non-alphabet elements. The function should use the modulo operator to handle edge cases where the shift goes past 'z' or 'Z'. Non-alphabet characters should be preserved in the resulting string.
"""

def advanced_cryptography(s, shift):
    shift = 3 * shift  
    result = ""

    for char in s:
        if 'A' <= char <= 'Z':
          result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
          result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
          result += char

    return result