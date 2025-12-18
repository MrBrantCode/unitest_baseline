"""
QUESTION:
Create a function `caesar_cipher_encrypt` that encrypts the string "hello world" using a Caesar cipher with a shift of 13 and assign the encrypted value to a variable named `greeting_message`. The function should preserve the case of the original text and only shift alphabetic characters.
"""

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text