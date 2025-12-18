"""
QUESTION:
Create a program that implements the Caesar cipher encryption and decryption algorithm. The program should have two functions: `caesar_encrypt(text, shift)` and `caesar_decrypt(text, shift)`, where `text` is the string to be encoded or decoded, and `shift` is the shift value.

The `caesar_encrypt(text, shift)` function should shift each letter in the input `text` by the specified `shift` value, while non-alphabetical characters should remain unchanged. The function should handle both uppercase and lowercase letters.

The `caesar_decrypt(text, shift)` function should perform the reverse operation of `caesar_encrypt(text, shift)`, shifting each letter in the input `text` by the negative of the specified `shift` value.

The shift value should be between 1 and 25.
"""

import string

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text