"""
QUESTION:
Create a function named `custom_caesar_cipher` that encrypts a given string using a custom Caesar cipher with a provided key. The function should handle both lowercase and uppercase letters, preserve the original case, and leave non-alphabetic characters unchanged. The key represents the number of positions each letter in the string should be shifted.
"""

def custom_caesar_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char

    return result