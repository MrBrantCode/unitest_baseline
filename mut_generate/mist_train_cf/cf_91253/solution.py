"""
QUESTION:
Implement a function named `caesar_cipher` that takes a string `message` and a positive integer `key` as input. The function should return the encrypted message as a string, using the Caesar cipher method where each letter in the plaintext is shifted a certain number of places down the alphabet. Non-alphabet characters should remain unchanged, and encryption should be case-sensitive.
"""

def caesar_cipher(message, key):
    encrypted_message = ""
    
    for char in message:
        if char.isupper():
            new_position = (ord(char) - 65 + key) % 26 + 65
            encrypted_message += chr(new_position)
        elif char.islower():
            new_position = (ord(char) - 97 + key) % 26 + 97
            encrypted_message += chr(new_position)
        else:
            encrypted_message += char
    
    return encrypted_message