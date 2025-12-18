"""
QUESTION:
Create a program with the following functions: 
- `encrypt_string(text, shift)`: Encrypts a given plain English string using the Caesar Cipher method with a provided integer shift value.
- `decrypt_string(text, shift)`: Decrypts a Caesar Cipher encrypted string back to its original form using the corresponding integer shift value.
- `calculate_shift(encrypted_text, original_text)`: Calculates the integer shift value used to create a Caesar Cipher encrypted string from a given original string.

Restrictions:
- The functions should handle both lowercase and uppercase letters, as well as non-alphabetic characters.
- The `calculate_shift` function should return the shift value if found, otherwise return `None`.
"""

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            char_encode = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += char_encode
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def caesar_cipher_calculate_shift(encrypted_text, original_text):
    for i in range(26):
        if caesar_cipher_encrypt(original_text, i) == encrypted_text:
            return i
    return None