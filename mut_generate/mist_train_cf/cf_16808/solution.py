"""
QUESTION:
Implement a function `caesar_cipher(message, key)` that encrypts a given message using the Caesar cipher. The function should take two parameters: `message`, a string of uppercase and lowercase alphabets, and `key`, a positive integer. The function should return the encrypted message as a string, leaving spaces and punctuation unchanged and preserving the case of the original letters. The length of the message will be between 1 and 10^6 characters, and the key will be between 1 and 10^6.
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