"""
QUESTION:
Implement the `caesar_cipher` function to encrypt a given message using the Caesar cipher with a specified key. The function should take a string message and a positive integer key as input, and return the encrypted message as a string. The encryption should be case-sensitive, leaving spaces and punctuation unchanged, and wrapping around the alphabet if the key exceeds the number of letters. The input message length will be between 1 and 10^6 characters, and the key will be between 1 and 10^6.
"""

def caesar_cipher(message, key):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message