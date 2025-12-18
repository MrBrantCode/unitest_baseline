"""
QUESTION:
Write a function named `caesar_cipher_encrypt` that takes two parameters: a string `text` and an integer `shift`. The function should return the encrypted string using a Caesar cipher with the specified shift. The function should handle both lowercase and uppercase letters, and leave non-alphabetic characters unchanged. Use this function to encrypt the string "hello world" with a shift of 13 and store the result in a variable named `greeting_message`.
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