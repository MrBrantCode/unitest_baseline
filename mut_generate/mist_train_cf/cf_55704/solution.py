"""
QUESTION:
Create a function `caesar_cipher_encryptor(input_string, key_shift)` that implements a monoalphabetic substitution cipher, also known as a Caesar Cipher, to encode the input string. The function should shift each lowercase letter in the input string by `key_shift` positions to the right, wrap around the alphabet if necessary, and leave non-alphabet characters unchanged. The function should return the encrypted string.
"""

def caesar_cipher_encryptor(input_string, key_shift):
    encrypted_string = ""
    for character in input_string:
        ascii_value = ord(character)
        if 97 <= ascii_value <= 122: 
            encrypted_string += chr( ( ascii_value - 97 + key_shift ) % 26 + 97 ) 
        else: 
            encrypted_string += character 
    return encrypted_string