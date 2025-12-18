"""
QUESTION:
Implement a function called `caesar_cipher` that takes a string `text` and an integer `shift` as input, and returns the encrypted string using the Caesar Cipher method. The function should only shift alphabetic characters and keep non-alphabetic characters unchanged. The shift operation should wrap around the alphabet if necessary.
"""

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result