"""
QUESTION:
Implement a function `xor_cipher` that takes two parameters: a text string to be encrypted or decrypted, and an optional key. If no key is provided, use 'ABCDEFG' as the default. The function should handle keys of any length and efficiently process large volumes of text. It should also be able to generate a random key of any specified length if needed. The function should return the encrypted or decrypted text.
"""

import os

def xor_cipher(text, key=None):
    if key is None:
        key = 'ABCDEFG'
        print(f"No key provided. Using default key '{key}'")
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    encrypt_decryption = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(text, key))
    return encrypt_decryption