"""
QUESTION:
Write a function `caesar_encrypt(text, shift)` that transforms a given string into uppercase and then encrypts it using the Caesar cipher with a given shift value between 1 and 25, inclusive. The function should replace each letter with another letter whose position in the alphabet is `shift` positions after the original letter, wrapping around to the start if necessary, and leave non-alphabet characters unchanged.
"""

def caesar_encrypt(text, shift):
    result = ''
    text = text.upper()
    for char in text:
        if 65 <= ord(char) <= 90:
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result