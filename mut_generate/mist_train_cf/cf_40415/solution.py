"""
QUESTION:
Implement the `encrypt(message, key)` and `decrypt(encrypted_message, key)` functions. 

The `encrypt(message, key)` function should take a message and a key as input, and return the encrypted message. The encryption algorithm involves shifting each character in the message based on the corresponding character in the key. If the key is shorter than the message, it should be repeated to match the length of the message. Non-alphabetic characters should remain unchanged.

The `decrypt(encrypted_message, key)` function should take an encrypted message and a key as input, and return the decrypted message. The decryption algorithm involves shifting each character in the encrypted message in the opposite direction based on the corresponding character in the key. If the key is shorter than the encrypted message, it should be repeated to match the length of the encrypted message. Non-alphabetic characters should remain unchanged.

Assume that the input message and encrypted message contain only printable ASCII characters.
"""

def encrypt(message, key):
    encrypted_message = ""
    key_length = len(key)
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            shift = ord(key[i % key_length]) - 96 if key[i % key_length].islower() else ord(key[i % key_length]) - 64
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    key_length = len(key)
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            shift = ord(key[i % key_length]) - 96 if key[i % key_length].islower() else ord(key[i % key_length]) - 64
            if char.islower():
                decrypted_message += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                decrypted_message += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_message += char
    return decrypted_message