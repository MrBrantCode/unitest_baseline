"""
QUESTION:
Implement the function `caesar_cipher(message, key)` that encrypts a given message using the Caesar cipher with the provided key. The function should take a string `message` and a positive integer `key` as input and return the encrypted message as a string. The encryption should be case-sensitive, and non-alphabet characters should be left unchanged. The key will be between 1 and 10^6, and the length of the message will be between 1 and 10^6 characters.
"""

def caesar_cipher(message, key):
    encrypted_message = ""

    for c in message:
        if c.isupper():
            encrypted_message += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        elif c.islower():
            encrypted_message += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted_message += c

    return encrypted_message