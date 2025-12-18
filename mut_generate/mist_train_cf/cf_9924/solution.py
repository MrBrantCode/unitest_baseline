"""
QUESTION:
Write a function `caesar_cipher_encrypt(text, key)` that implements a Caesar Cipher encryption algorithm. The function should shift each letter in the input `text` by the specified `key` positions, while preserving the case of the letters, and leave non-alphabetic characters (such as punctuation and spaces) unchanged. The shift should wrap around the alphabet if necessary, i.e., 'z' shifted by 1 becomes 'a' and 'Z' shifted by 1 becomes 'A'.
"""

def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate shift based on uppercase or lowercase
            if char.isupper():
                shift = ord('A')
            else:
                shift = ord('a')
            # Encrypt the character
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            # Append punctuation and spaces as is
            encrypted_text += char
    return encrypted_text